### Problem1:"1 error:src refspec master does not match any"
 some forder does not has any file

### create new repository and push local code
* create new repository xxx in github.com
* locally, create directory xxx and cd xxx
* exe git init, indicate this dir is git dir
* git config --global user.email "38842860@qq.com"
* git config --global user.username "tramsyck"
* copy ssh public key to github
* git remote add origin git@github.com:tramsyck/xxx.git
* git push -u origin master，commit local code to github


# 分支操作
## 创建分支
   git branch xxx
## 切换分支
   git checkout xxx
## 合并分支
   切换到目标分支,git checkout master
   执行合并：git merge xxx
## 删除分支
   git branch -d xxx
## 提交远程分支
   出现当前版本较早，可以这样做
   
   +  git push origin develop -f选项
