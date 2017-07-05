##Problem1:"1 error:src refspec master does not match any"
 some forder does not has any file

##create new repository and push local code
1、create new repository xxx in github.com
2、locally, create directory xxx and cd xxx
3. exe git init, indicate this dir is git dir
4. git config --global user.email "38842860@qq.com"
5. git config --global user.username "tramsyck"
6. copy ssh public key to github
7. git remote add origin git@github.com:tramsyck/xxx.git
8. git push -u origin master，commit local code to github
