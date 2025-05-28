set shell := ["nu", "-c"]

# list available recipes
list:
    @just --list

    
sendgit:
    git add .
    git commit -m yeet
    git push --force
