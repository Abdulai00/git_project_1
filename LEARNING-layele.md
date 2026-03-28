## LEARNINGS-layele

## Checkpoint one
git add . 
git commit -m "fixed"
git add . 
git commit -m "update"

## Reflection 
I learned that I can change a file and vale multiple commits without interacting with the github repo. 

## Checkpoint two 
git log --oneline
git revert <hash>

## Reflection 
I learned that I undo the changes made by a commit while also remember that I made that commit so in future case I can come back to edit it or find out if I made an error in that commit.


## Checkpoint Three 
git cherry-pick <hash>
git reset --hard HEAD~1

## Reflection 
I learned that I can move one commit from one branch to another commit from another branch and remove it at well. Additionally, I learned how to resolve conflict. 

## Checkpoint Four 
git checkout -b experiment/layele
git branch -D experiment/layele
git reflog
git checkout -b recovered/layele <hash from reflog>
git merge recovered/layele

## Reflection 
I learned that I can accidently delete a branch. However, that don't mean that work I made goes away too. Rather that I can recover it  by find out which hash did the deleting than making a new branch so that it can have the work of the deleted branch. Also learned how to merge the branchs. 

## Checkpoint Five
git remote add upstream <url>
git fetch upstream
git checkout main
git merge upstream/main
git checkout feature/layele
git rebase main
git push --force-with-lease origin feature/layele

## Reflection
I learned that I can keep two origin branchs for the forked repo and upstream for the original repo. Which lets me pull in changes from the original. Than I can rebase it to main  to keeps my branch history and prevent conflicts. 


## Checkpoint Six
git log main..HEAD --oneline
git rebase -i main
git push --force-with-lease origin feature/layele

## Reflection 
I learned that I can go back and edit my commit history. This allows me to have weird but understandable commit on my local repo and rewrite it for when I push it to digital repo. Allowing me to clear up my commit history to be more professional.


## Checkpoint seven 
I learned to look over my teamate code as some case it isn't going to work with mine. Therefore I have to go ahead and remove or integrate their code to prevent or resolve conflicts. 

