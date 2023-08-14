## 공군 신체사이즈 사후분포 예측 코드

setwd("C:/Class/3-1/Bayesian Statistics/Team/CSV")

## HPD구할 때 사용할 함수 정의
HPDgrid=function(prob, level=0.95){
  prob.sort=sort(prob, decreasing=T)
  M=min(which(cumsum(prob.sort)>=level))
  height=prob.sort[M]
  HPD.index=which(prob >= height)
  HPD.level=sum(prob[HPD.index])
  res=list(index=HPD.index, level=HPD.level)
  return(res)
}

## 남자 군인 하의 수치(1분기 2분기)

m_dataset1 <- read.csv('국방부_공군 신체측정정보(남)_1분기(0304).csv')
average_m1 <- m_dataset1$average_m

m_dataset2 <- read.csv('국방부_공군 신체측정정보(남)_2분기(0616).csv')
average_m2 <- m_dataset2$average_m

"
## 로그변환 전 정규성 검정 Shapiro test
x1=average_m1
hist(x1)
a <- qqnorm(x1)
qqline(x1)
shapiro.test(x1)
## 로그변환 전 정규성 검정 Shapiro test
x2=average_m2
hist(x2)
a <- qqnorm(x2)
qqline(x2)
shapiro.test(x2)
"

par(mfrow = c(1,2))

## 로그변환 후 정규성 검정 Shapiro test
average_log1 <- log(average_m1 + 1)
x1=average_log1
hist(average_log1, main='m_log(average_m1+1) hist')
qqnorm(x1)
qqline(x1)
shapiro.test(x1) 

## 로그변환 후 정규성 검정 Shapiro test
average_log2 <- log(average_m2 + 1)
x2=average_log2
hist(average_log2, main='m_log(average_m2+1) hist')
qqnorm(x2)
qqline(x2)
shapiro.test(x2) 


## 사전평균, 사후평균 구하기(log된 값) 
## Theta의 사전분포 ~ N(mu0, s0)
mu0=log(mean(average_m1)); s0= log(sd(average_m1)); n= 330; xbar = log(mean(average_m2)); s = log(sd(average_m2))
mu0; s0; #사전분포 정의
xbar; s; #관측치 정의

(w=(1+s^2/(n*s0^2))^{-1}) #w
(mu.post=w*xbar+(1-w)*mu0) #사후 평균
(s.post=sqrt(w*s^2/n)) #사후 표준편차
s.post^2 #사후 분산
## Theta의 사후분포 ~ N(mu.post, s.post^2)

## 사전분포와 사후분포 Plot
par(mfrow = c(1,1))
theta=seq(mu.post-5*s.post,mu.post+5*s.post,length=100)
plot(theta,dnorm(theta,mu.post,s.post),type='l',main='posterior and prior of theta')
lines(theta,dnorm(theta,mu0,s0),lty=2,col=2)
legend(4.8, 3,c('posterior','prior'),lty=1:2,col=1:2)

## predictive for x(new) 분산이 알려졌을 때, X(n+1)의 예측분포 ~ N(mu.new, s.new)
(mu.new=mu.post) 
(s.new=sqrt(s^2+s.post^2)) 
x.new=seq(mu.new-5*s.new,mu.new+5*s.new,length=100)
plot(x.new,dnorm(x.new,mu.new,s.new),type='l',main='predictive density of x(new)')

## <지수변환 했을 때>predictive for x(new) 분산이 알려졌을 때, X(n+1)의 예측분포 ~ N(mu.new, s.new)
(mu.new=exp(mu.post)) 
(s.new=sqrt((e^s)^2+exp(s.post^2))) 
x.new=seq(mu.new-5*s.new,mu.new+5*s.new,length=100)
plot(x.new,dnorm(x.new,mu.new,s.new),type='l',main='predictive density of x(new) compare', ylim = c(0,0.07), ylab = ' ')
par(new=TRUE)
plot(x.new,dnorm(x.new,mean(average_m1),sd(average_m1)), type='l', col=2, ylim = c(0,0.07), ylab = ' ')
legend(115, 0.06,c('posterior','prior'),lty=1:1,col=1:4)

## 격자점을 이용한 최대사후구간
theta=seq(-5,15,length=100001) 
ftheta=dnorm(theta,mu.post,s.post)
prob=ftheta/sum(ftheta)
HPD1=HPDgrid(prob, 0.95)
HPD1.grid=c(min(theta[HPD1$index]),max(theta[HPD1$index]))
dnorm(HPD1.grid,mu.post,s.post) 
plot(theta,dnorm(theta,mu.post,s.post),type='l',xlab=expression(theta), main='HPD Interval grid', ylab=expression(paste(pi,'(',theta,'|x)')), xlim = c(4,5))
abline(v=c(HPD1.grid[1], HPD1.grid[2]),lty=2,col=2) 
HPD1.grid
HPD1$level
legend(4.8, 3,c('HPD interval grid'),lty=2,col=2)


## 사후분위수를 이용한 최대사후구간
lc=qnorm(0.025,mu.post,s.post)
uc=qnorm(0.975,mu.post,s.post) 
c(lc,uc)
dnorm(c(lc,uc),mu.post,s.post) 
plot(theta,dnorm(theta,mu.post,s.post),type='l',xlab=expression(theta), main='HPD grid',
     ylab=expression(paste(pi,'(',theta,'|x)')), , xlim = c(4,5))

## 사후분위수, 격자점 최대사후구간, 고전적 신뢰구간 비교
abline(v=c(lc,uc),lty=1,lwd = 2,col=2)
abline(v=c(HPD1.grid[1],HPD1.grid[2]),lty=2, lwd = 3,col=4) 
abline(v=c(mu.post - (1.96 * s.post),mu.post + (1.96 * s.post)),lty=2, lwd = 3,col=3)

c(mu.post - (1.96 * s.post),mu.post + (1.96 * s.post))
legend(4.8,3,c('HPD grid','CI asympototic', 'CI exact'),lty=c(2,4, 2),col=c(2,4, 3))

