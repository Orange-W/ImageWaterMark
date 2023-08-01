# ImageWaterMark

使用图像标序，代替明码水印。

## 样例
![xxx](./headimg/dstimage/result_head_img_index0.png)

在用户头像周围放上了标记。每个标记可记录 64 bit。如一个 16位 id 图像只需要 4个标记图。

上述图片共 16 位，和下面等价。

0x0001 0203 0506 0708 0910 1112 1314 1516



## 解码图
![xxx](./result.png)
