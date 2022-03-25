### 一：Git工作流程
1. git仓库(版本区)
存放提交记录
2. 暂存区
临时存放杯修改的文件
3. 工作区
被git管理的目录

### 二：Git使用前配置
1. 配置提交人姓名：
git config --global user.name “提交人姓名”  # 对当前系统用户有效

2. 配置提交人姓名：
git config --global user.email “提交人邮箱” # 对当前系统用户有效
（作用：识别开发人员，与登陆github的账户无关）

3. 查看git配置信息：git config --list
> ps:
    1. 如果要对配置信息进行修改，重复上述命令即可。
    2. 配置只需要执行一次。

### 三：常用提交步骤
>tips:
mkdir name :在当前目录下新建一个名字为name的文件夹
pwd : 当前目录
ls -ah:展示当前目录下所有文件

1. 初始化git仓库
git init # 把当前目录变成Git可以管理的仓库

2. 查看仓库状态：
git status

3. 追踪文件
git add name

4. 向仓库中提交代码(提交当前目录下的全部文件)
git commit -m “提交信息” # 提交所有 add
vs： git commit -m "提交信息" 文件 # 提交某个文件
ps：提交只会提交add完成后的文件

5. 显示提交记录
git log
>补充： 
git log --pretty=oneline # 一行显示版本信息 
git log lfa380b5O2a0Ob82bfc8d84c5ab5el5b8fbf7dac # 会显示所有关于这个id以及之前的修改记录 
git log lfa380b5O2a0Ob82bfc8d84c5ab5el5b8fbf7dac -1 
加上-1参数表示我们只想看到一行记录 而如果想要查看这条提交记录具体修改了什么内容，可以在命令中加入p参数，
命令如下: git log Ifa380b502a00b82bfc8d84c5ab5el5b8fbf7dac -1 -p

6. 回退版本
git reset --hard 版本id #
当前版本为 HEAD
上一个版本为 HEAD^
往上100个版本为 HEAD~100。

7. 查看版本信息
git reflog # 记录所有操作信息，可用于版本回退

8. 查看未使用add命令时的修改
git diff #
这样可以查看到所有文件的更改内容，如果你只想查看MainActivity.java这个文件的更改内容
可以使用如下命令：
git diff MainActivity.java
vs：git log 表示最近的改变
git reflog 可以看到所有的改变 如果文件未被跟踪,即没有使用git add这个命令时,文件为红色,如果使用这个命令,则文件变为绿色.

9. 撤销
    1. git checkout -- 文件
    （ --很重要，没有--，就变成了“切换到另一个分支”的命令）
    不过这种撤销方式只适用于那些还没有执行过add命令的文件.

    2. 如果某个文件已经被添加过了，这种方式就无法撤销其更改的内容. 这种情况我们应该先对其取消添加，然后才可以撤回提交。取消添加使用的是reset命令，用法如下所示：
        * git reset HEAD 文件
        然后再运行一遍git status命令，你就会发现MainActivity.java这个文件重新变回了未添加状态，此时就可以使用checkout命令来将修改的内容进行撤销了。

        * 将文件从暂存区中删除： git rm --cached 文件
        应用场景:开发过程中,不是每个文件都是有必要交给git管理的,使用这个命令可以从暂存区删除没用的文件,不交给git管理,此时文件在工作目录依然存在,只是没在暂存区而已.

        * 将 git 仓库中指定的更新记录恢复出来，并且覆盖暂存区和工作目录：git reset --hard commitID
        应用场景:开发过程中,如果想要利用某次记录覆盖暂存区和工作目录,则可以使用 上面那个命令.

10. 删除
    提交过了的文件:
    1. 从文件夹中删除:
    rm 该文件
    2. 从版本库中删除：
        2.1 命令git rm删掉；
        2.2 git commit;
    
