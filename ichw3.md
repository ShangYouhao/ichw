##计概作业三  
###高速缓冲存储器(Cache)  
  
####结构  
由三大部分组成：  
_Cache存储体：_存放调入的指令和数据块  
_地址转换部件：_建立联系主存地址和缓存地址的目录  
_替换部件：_进行数据块替换并修改地址转换信息  
####工作原理  
Cache作为比主存快得多但容量小的多的储存器件，在CPU和主存间起到缓冲的作用。  
Cache中暂时存储着相对少量但使用频率高的数据块，从而提高数据存储的平均速度。  
工作步骤：  
CPU访问Cache——>需要的数据块在cache里——>命中——>存取数据  
(或者) CPU访问Cache——>需要的数据块不在Cache里——>从内存中复制需要的数据块到Cache里——>存取数据  
地址映像方法：  
直接映像 每个数据块必须存储在Cache的固定对应区域  
全相连映像 将主存与Cache均划为相同大小的区域，每块区域整存整取  
组相连映像 将上述的区域再划分为组，组内采用全相连映像，组的编号采用直接映像方式
