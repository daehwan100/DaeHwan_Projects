import gradio as gr
import argparse
import gdown
import cv2
import numpy as np
import os
import sys
sys.path.append(sys.path[0]+"/tracker")
sys.path.append(sys.path[0]+"/tracker/model")
from Tracking_XMem import Tracking_Sam
from Tracking_XMem import parse_augment
import requests
import json
import torchvision
import torch 
from tools.painter import mask_painter
import psutil
import time
from PIL import Image

# 포인트 입력 프롬프트 상태로 변환
def get_prompt(click_state, click_input):
    inputs = json.loads(click_input)
    points = click_state[0]
    labels = click_state[1]
    for input in inputs:
        points.append(input[:2])
        labels.append(input[2])
    click_state[0] = points
    click_state[1] = labels
    prompt = {
        "prompt_type":["click"],
        "input_point":click_state[0],
        "input_label":click_state[1],
        "multimask_output":"True",
    }
    return prompt


# 업로드 비디오에서 프레임 추출
def get_frames_from_video(video_input, video_state):
    video_path = video_input
    frames = []
    user_name = time.time()
    operation_log = [("",""),("영상분석 완료. 추적할 인물을 선택해주세요.","Normal")]
    try:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == True:
                current_memory_usage = psutil.virtual_memory().percent
                frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if current_memory_usage > 90:
                    operation_log = [("Memory usage >90%. 비디오 크기를 줄이세요.", "Error")]
                    print("Memory usage >90%. 비디오 크기를 줄이세요.")
                    break
            else:
                break
    except (OSError, TypeError, ValueError, KeyError, SyntaxError) as e:
        print("read_frame_source:{} error. {}\n".format(video_path, str(e)))
    image_size = (frames[0].shape[0],frames[0].shape[1]) 
    # 비디오(video_state) initialize 
    video_state = {
        "user_name": user_name,
        "video_name": os.path.split(video_path)[-1],
        "origin_images": frames,
        "painted_images": frames.copy(),
        "masks": [np.zeros((frames[0].shape[0],frames[0].shape[1]), np.uint8)]*len(frames),
        "logits": [None]*len(frames),
        "select_frame_number": 0,
        "fps": fps
        }
    video_info = "Video Name: {}, FPS: {}, Total Frames: {}, Image Size:{}".format(video_state["video_name"], video_state["fps"], len(frames), image_size)
    model.samcontroler.sam_controler.reset_image() 
    model.samcontroler.sam_controler.set_image(video_state["origin_images"][0])
    return video_state, video_info, video_state["origin_images"][0], gr.update(visible=True, maximum=len(frames), value=1), gr.update(visible=True, maximum=len(frames), value=len(frames)), \
                        gr.update(visible=True),\
                        gr.update(visible=True), gr.update(visible=True), \
                        gr.update(visible=True), gr.update(visible=True), \
                        gr.update(visible=True), gr.update(visible=True), \
                        gr.update(visible=True), gr.update(visible=True), \
                        gr.update(visible=True, value=operation_log)

def run_example(example):
    return video_input

# gradio에서 선택한 프레임 가져오기
def select_template(image_selection_slider, video_state, interactive_state, mask_dropdown):

    # images = video_state[1]
    image_selection_slider -= 1
    video_state["select_frame_number"] = image_selection_slider

    # 선택 이미지 SAM에 넣기
    model.samcontroler.sam_controler.reset_image()
    model.samcontroler.sam_controler.set_image(video_state["origin_images"][image_selection_slider])

    # 마스크 업데이트
    if mask_dropdown:
        print("ok")
    operation_log = [("",""), ("프레임 선택 {}. 트랙킹할 이미지를 클릭하거나 mask를 추가하세요.".format(image_selection_slider),"Normal")]


    return video_state["painted_images"][image_selection_slider], video_state, interactive_state, operation_log

# tracking 끝 프레임 지정하기
def get_end_number(track_pause_number_slider, video_state, interactive_state):
    interactive_state["track_end_number"] = track_pause_number_slider
    operation_log = [("",""),("프레임에서 tracking 끝 설정 {}".format(track_pause_number_slider),"Normal")]

    return video_state["painted_images"][track_pause_number_slider],interactive_state, operation_log

def get_resize_ratio(resize_ratio_slider, interactive_state):
    interactive_state["resize_ratio"] = resize_ratio_slider

    return interactive_state

# SAM으로 mask하기
def sam_refine(video_state, point_prompt, click_state, interactive_state, evt:gr.SelectData):
    """
    Args:
        template_frame: PIL.Image
        point_prompt: flag for positive or negative button click
        click_state: [[points], [labels]]
    """
    if point_prompt == "Positive":
        coordinate = "[[{},{},1]]".format(evt.index[0], evt.index[1])
        interactive_state["positive_click_times"] += 1
    else:
        coordinate = "[[{},{},0]]".format(evt.index[0], evt.index[1])
        interactive_state["negative_click_times"] += 1
    
    # sam 모델 
    model.samcontroler.sam_controler.reset_image()
    model.samcontroler.sam_controler.set_image(video_state["origin_images"][video_state["select_frame_number"]])
    prompt = get_prompt(click_state=click_state, click_input=coordinate)

    mask, logit, painted_image = model.first_frame_click( 
                                                      image=video_state["origin_images"][video_state["select_frame_number"]], 
                                                      points=np.array(prompt["input_point"]),
                                                      labels=np.array(prompt["input_label"]),
                                                      multimask=prompt["multimask_output"],
                                                      )
    video_state["masks"][video_state["select_frame_number"]] = mask
    video_state["logits"][video_state["select_frame_number"]] = logit
    video_state["painted_images"][video_state["select_frame_number"]] = painted_image

    # mask_image = mask.astype(np.uint8)
    # logit_image = logit.astype(np.uint8)

    # mask_image = Image.fromarray(mask_image)
    # logit_image = Image.fromarray(logit_image)
    mask_3 = np.repeat(mask[..., np.newaxis], 3, axis=2)
    mask_3 = mask_3.astype(bool)

    # img_arr = np.array(painted_image)
    img_arr = np.array(video_state["origin_images"][video_state["select_frame_number"]])

    true_values = np.where(mask_3, img_arr, 255)
    true_values_ = true_values.astype(np.uint8)
    true_values__ = Image.fromarray(true_values_)

    image_save_path = os.path.join('/content/drive/MyDrive/MIA_TRACKING_7조/result', "Find_image.png")

    # 이미지 저장
    true_values__.save(image_save_path)

    operation_log = [("",""), ("추적할 인물을 선택하였습니다.","Normal")]

    return painted_image, video_state, interactive_state, operation_log


# SAM으로 mask하기
def sam_refine_2(video_state, point_prompt, click_state, interactive_state, evt:gr.SelectData):
    """
    Args:
        template_frame: PIL.Image
        point_prompt: flag for positive or negative button click
        click_state: [[points], [labels]]
    """
    if point_prompt == "Positive":
        coordinate = "[[{},{},1]]".format(evt.index[0], evt.index[1])
        interactive_state["positive_click_times"] += 1
    else:
        coordinate = "[[{},{},0]]".format(evt.index[0], evt.index[1])
        interactive_state["negative_click_times"] += 1
    
    # sam 모델 
    model.samcontroler.sam_controler.reset_image()
    model.samcontroler.sam_controler.set_image(video_state["origin_images"][video_state["select_frame_number"]])
    prompt = get_prompt(click_state=click_state, click_input=coordinate)

    mask, logit, painted_image = model.first_frame_click( 
                                                      image=video_state["origin_images"][video_state["select_frame_number"]], 
                                                      points=np.array(prompt["input_point"]),
                                                      labels=np.array(prompt["input_label"]),
                                                      multimask=prompt["multimask_output"],
                                                      )
    video_state["masks"][video_state["select_frame_number"]] = mask
    video_state["logits"][video_state["select_frame_number"]] = logit
    video_state["painted_images"][video_state["select_frame_number"]] = painted_image
    paint_test = video_state["painted_images"][video_state["select_frame_number"]]
    operation_log = [("",""), ("추적할 인물을 선택하였습니다.","Normal")]

    return painted_image, video_state, interactive_state, operation_log, paint_test



def add_multi_mask(video_state, interactive_state, mask_dropdown):
    try:
        mask = video_state["masks"][video_state["select_frame_number"]]
        interactive_state["multi_mask"]["masks"].append(mask)
        interactive_state["multi_mask"]["mask_names"].append("mask_{:03d}".format(len(interactive_state["multi_mask"]["masks"])))
        mask_dropdown.append("mask_{:03d}".format(len(interactive_state["multi_mask"]["masks"])))
        select_frame, run_status = show_mask(video_state, interactive_state, mask_dropdown)

        operation_log = [("",""),("tracking할 mask 추가.","Normal")]
    except:
        operation_log = [("mask를 생성하려면 왼쪽 이미지를 클릭하세요.", "Error"), ("","")]
    return interactive_state, gr.update(choices=interactive_state["multi_mask"]["mask_names"], value=mask_dropdown), select_frame, [[],[]], operation_log

def clear_click(video_state, click_state):
    click_state = [[],[]]
    template_frame = video_state["origin_images"][video_state["select_frame_number"]]
    operation_log = [("",""), ("point기록 모두 삭제.","Normal")]
    return template_frame, click_state, operation_log

def remove_multi_mask(interactive_state, mask_dropdown):
    interactive_state["multi_mask"]["mask_names"]= []
    interactive_state["multi_mask"]["masks"] = []

    operation_log = [("",""), ("모든 mask를 지우고 새로운 mask를 생성하세요.","Normal")]
    return interactive_state, gr.update(choices=[],value=[]), operation_log

def show_mask(video_state, interactive_state, mask_dropdown):
    mask_dropdown.sort()
    select_frame = video_state["origin_images"][video_state["select_frame_number"]]
    for i in range(len(mask_dropdown)):
        mask_number = int(mask_dropdown[i].split("_")[1]) - 1
        mask = interactive_state["multi_mask"]["masks"][mask_number]
        select_frame = mask_painter(select_frame, mask.astype('uint8'), mask_color=mask_number+2)
    
    operation_log = [("",""), ("Select {} for tracking".format(mask_dropdown),"Normal")]
    return select_frame, operation_log

# tracking vos
def vos_tracking_video(video_state, interactive_state, mask_dropdown):
    operation_log = [("",""), ("인물 추적이 완료되었습니다.","Normal")]
    model.xmem.clear_memory()

    tracked_timestamps = []
    if interactive_state["track_end_number"]:
        following_frames = video_state["origin_images"][video_state["select_frame_number"]:interactive_state["track_end_number"]]
    else:
        following_frames = video_state["origin_images"][video_state["select_frame_number"]:]

    for i, frame in enumerate(following_frames):
        is_tracked = True  # 트래킹 알고리즘 결과
        if is_tracked:
            timestamp = (video_state["select_frame_number"] + i) / video_state["fps"]
            tracked_timestamps.append(timestamp)


    if interactive_state["multi_mask"]["masks"]:
        if len(mask_dropdown) == 0:
            mask_dropdown = ["mask_001"]
        mask_dropdown.sort()
        template_mask = interactive_state["multi_mask"]["masks"][int(mask_dropdown[0].split("_")[1]) - 1] * (int(mask_dropdown[0].split("_")[1]))
        for i in range(1,len(mask_dropdown)):
            mask_number = int(mask_dropdown[i].split("_")[1]) - 1 
            template_mask = np.clip(template_mask+interactive_state["multi_mask"]["masks"][mask_number]*(mask_number+1), 0, mask_number+1)
        video_state["masks"][video_state["select_frame_number"]]= template_mask
    else:      
        template_mask = video_state["masks"][video_state["select_frame_number"]]
    fps = video_state["fps"]

    # operation error
    if len(np.unique(template_mask))==1:
        template_mask[0][0]=1
        operation_log = [("Error! tracking하기 위해서는 적어도 하나의 mask를 생성하세요.","Error"), ("","")]
    masks, logits, painted_images = model.generator(images=following_frames, template_mask=template_mask) 

    # clear
    model.xmem.clear_memory()

    if interactive_state["track_end_number"]: 
        video_state["masks"][video_state["select_frame_number"]:interactive_state["track_end_number"]] = masks
        video_state["logits"][video_state["select_frame_number"]:interactive_state["track_end_number"]] = logits
        video_state["painted_images"][video_state["select_frame_number"]:interactive_state["track_end_number"]] = painted_images
    else:
        video_state["masks"][video_state["select_frame_number"]:] = masks
        video_state["logits"][video_state["select_frame_number"]:] = logits
        video_state["painted_images"][video_state["select_frame_number"]:] = painted_images

    video_output = generate_video_from_frames(video_state["painted_images"], output_path="./result/track/{}".format(video_state["video_name"]), fps=fps) # import video_input to name the output video

    interactive_state["inference_times"] += 1
    
    print("For generating this tracking result, inference times: {}, click times: {}, positive: {}, negative: {}".format(interactive_state["inference_times"], 
                                                                                                                                           interactive_state["positive_click_times"]+interactive_state["negative_click_times"],
                                                                                                                                           interactive_state["positive_click_times"],
                                                                                                                                        interactive_state["negative_click_times"]))

    #### mask 저장 code
    if interactive_state["mask_save"]:
        if not os.path.exists('/content/drive/MyDrive/MIA_TRACKING_7조/result/mask/{}'.format(video_state["video_name"].split('.')[0])):
            os.makedirs('/content/drive/MyDrive/MIA_TRACKING_7조/result/mask/{}'.format(video_state["video_name"].split('.')[0]))
        i = 0
        print("save mask")
        for mask in video_state["masks"]:
            np.save(os.path.join('/content/drive/MyDrive/MIA_TRACKING_7조/result/mask/{}'.format(video_state["video_name"].split('.')[0]), '{:05d}.npy'.format(i)), mask)
            i+=1
    #### mask 저장 code
    return video_output, video_state, interactive_state, operation_log

# generate video after vos inference
def generate_video_from_frames(frames, output_path, fps=30):
    # video.release()
    frames = torch.from_numpy(np.asarray(frames))
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    torchvision.io.write_video(output_path, frames, fps=fps, video_codec="libx264")
    return output_path

from PIL import Image

# track_anything.py
args = parse_augment()

xmem_checkpoint = "XMem-s012.pth"
xmem_checkpoint_url = "https://github.com/hkchengrex/XMem/releases/download/v1.0/XMem-s012.pth"

SAM_checkpoint = "/content/drive/MyDrive/MIA_TRACKING_7조/checkpoints/MIA_tracking_2.pth"
xmem_checkpoint = "/content/drive/MyDrive/MIA_TRACKING_7조/checkpoints/XMem-s012.pth"

# initialize sam, xmem 모델
model = Tracking_Sam(SAM_checkpoint, xmem_checkpoint,args)

title = """<p><h1 align="center">MIA Tracking</h1></p>
    """
description = """<p><p align="center"> Tracking기반 지능형 미아 방지 시스템입니다.</p></p>"""


with gr.Blocks() as iface:
    """
        state for 
    """
    click_state = gr.State([[],[]])
    interactive_state = gr.State({
        "inference_times": 0,
        "negative_click_times" : 0,
        "positive_click_times": 0,
        "mask_save": args.mask_save,
        "multi_mask": {
            "mask_names": [],
            "masks": []
        },
        "track_end_number": None,
        "resize_ratio": 1
    }
    )

    video_state = gr.State(
        {
        "user_name": "",
        "video_name": "",
        "origin_images": None,
        "painted_images": None,
        "masks": None,
        "inpaint_masks": None,
        "logits": None,
        "select_frame_number": 0,
        "fps": 30
        }
    )
    gr.Markdown(title)
    gr.Markdown(description)
    with gr.Row():
        # 비디오 input
        with gr.Column():
            with gr.Row(scale=0.4):
                video_input = gr.Video(autosize=True)
                with gr.Column():
                    video_info = gr.Textbox(label="영상 분석")
          

            with gr.Row():
                with gr.Column():
                    # 프레임 추출
                    with gr.Column():
                        extract_frames_button = gr.Button(value="영상 분석", interactive=True, variant="secondary")

                    with gr.Row():
                        with gr.Row():
                            point_prompt = gr.Radio(
                                choices=["Positive"],
                                value="Positive",
                                label="Point prompt",
                                interactive=True,
                                visible=False)
                            remove_mask_button = gr.Button(value="Delete masks", interactive=True, visible=False) 
                            clear_button_click = gr.Button(value="Clear points", interactive=True, visible=False).style(height=160)
                            Add_mask_button = gr.Button(value="Add mask", interactive=True, visible=False)

                    template_frame = gr.Image(type="pil", interactive=True, elem_id="template_frame", visible=False).style(height=360)
                    # template_frame_2 = gr.Image(type="pil",interactive=True, elem_id="template_frame", visible=True).style(height=240)

                    # template_frame_2 = gr.Image(type="pil",interactive=True, elem_id="video_state", visible=False).style(height=130)
                    # gr.Image(type="pil", painted_image)

                    image_selection_slider = gr.Slider(minimum=1, maximum=100, step=1, value=1, label="Track start frame", visible=False)
                    track_pause_number_slider = gr.Slider(minimum=1, maximum=100, step=1, value=1, label="Track end frame", visible=False)


                with gr.Column():
                    run_status = gr.HighlightedText(value=[("Text","Error"),("to be","Label 2"),("highlighted","Label 3")], visible=False)
                    mask_dropdown = gr.Dropdown(multiselect=True, value=[], label="Mask selection", info=".", visible=False)
                    video_output = gr.Video(autosize=True, visible=False).style(height=360)
                    with gr.Row():
                        tracking_video_predict_button = gr.Button(value="Tracking", visible=False)


    # 1번째 단계: 비디오 정보 얻기
    extract_frames_button.click(
        fn=get_frames_from_video,
        inputs=[
            video_input, video_state
        ],
        outputs=[video_state, video_info, template_frame,
                 image_selection_slider, track_pause_number_slider,point_prompt, clear_button_click, Add_mask_button, template_frame,
                 tracking_video_predict_button, video_output, mask_dropdown, remove_mask_button, run_status]
    )   

    # 2번째 단계: 추적 이미지 선택하기
    image_selection_slider.release(fn=select_template, 
                                   inputs=[image_selection_slider, video_state, interactive_state], 
                                   outputs=[template_frame, video_state, interactive_state, run_status], api_name="select_image")
    track_pause_number_slider.release(fn=get_end_number, 
                                   inputs=[track_pause_number_slider, video_state, interactive_state], 
                                   outputs=[template_frame, interactive_state, run_status], api_name="end_image")

    # sam을 통해서 선택한 인물
    template_frame.select(
        fn=sam_refine,
        inputs=[video_state, point_prompt, click_state, interactive_state],
        outputs=[template_frame, video_state, interactive_state, run_status]
    )

    # 다른 인물 추가할때
    Add_mask_button.click(
        fn=add_multi_mask,
        inputs=[video_state, interactive_state, mask_dropdown],
        outputs=[interactive_state, mask_dropdown, template_frame, click_state, run_status]
    )

    remove_mask_button.click(
        fn=remove_multi_mask,
        inputs=[interactive_state, mask_dropdown],
        outputs=[interactive_state, mask_dropdown, run_status]
    )

    # 선택된 인물 추적
    tracking_video_predict_button.click(
        fn=vos_tracking_video,
        inputs=[video_state, interactive_state, mask_dropdown],
        outputs=[video_output, video_state, interactive_state, run_status]
    )
    
    # mask 클릭
    mask_dropdown.change(
        fn=show_mask,
        inputs=[video_state, interactive_state, mask_dropdown],
        outputs=[template_frame, run_status]
    )
    
    
    # input 삭제
    video_input.clear(
        lambda: (
        {
        "user_name": "",
        "video_name": "",
        "origin_images": None,
        "painted_images": None,
        "masks": None,
        "inpaint_masks": None,
        "logits": None,
        "select_frame_number": 0,
        "fps": 30
        },
        {
        "inference_times": 0,
        "negative_click_times" : 0,
        "positive_click_times": 0,
        "mask_save": args.mask_save,
        "multi_mask": {
            "mask_names": [],
            "masks": []
        },
        "track_end_number": 0,
        "resize_ratio": 1
        },
        [[],[]],
        None,
        None,
        gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), \
        gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), \
        gr.update(visible=False), gr.update(visible=False), gr.update(visible=False, value=[]), gr.update(visible=False), \
        gr.update(visible=False), gr.update(visible=False)
                        
        ),
        [],
        [ 
            video_state,
            interactive_state,
            click_state,
            video_output,
            template_frame,
            tracking_video_predict_button, image_selection_slider , track_pause_number_slider,point_prompt, clear_button_click, 
            Add_mask_button, template_frame, tracking_video_predict_button, video_output, mask_dropdown, remove_mask_button, run_status
        ], 
        queue=False,
        show_progress=False)

    # 포인트 삭제
    clear_button_click.click(
        fn = clear_click,
        inputs = [video_state, click_state,],
        outputs = [template_frame,click_state, run_status],
    )
    
iface.queue(concurrency_count=1)
iface.launch(debug=True, enable_queue=True)
