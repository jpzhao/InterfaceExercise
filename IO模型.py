# -*- coding: utf-8 -*-
'''
IO模型都是针对网络IO的
Stevens在文章中一共比较了五中IO Model:
blocking IO       阻塞IO
nonblocking IO    非阻塞IO
IO nultiplexing   IO多路复用
signal driven IO  信号驱动IO
asychronous IO    异步IO
由signal driven IO(信号驱动IO)在实际中并不常用，所以主要介绍其余四种IO Mode.
#1)等待数据准备(Waiting for the data to be ready)
#2)将数据从内核拷贝到进程中(Copying the data from the kernel to the process)
同步异步
阻塞非阻塞
常见的网络阻塞状态：
accept
recv
recvfrom
send虽然它也有IO行为，但是不在我们的考虑范围
'''