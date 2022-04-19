Data_frame <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

)
Data_frame_new <- Data_frame[-c(1),-c(1)]