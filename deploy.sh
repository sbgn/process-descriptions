#!/bin/bash
# See https://medium.com/@nthgergo/publishing-gh-pages-with-travis-ci-53a8270e87db
set -o errexit

rm -rf tmp && mkdir tmp

# config
git config --global user.name ${GIT_NAME} && git config --global user.email ${GIT_EMAIL}

# deploy
cd tmp && mkdir travis && cp $TRAVIS_BUILD_DIR/Specification/*.pdf travis

git init && git add . && git commit -m "Deploy"
git push --force --quiet "https://${GITHUB_TOKEN}@$github.com/${GITHUB_REPO}.git" master:gh-pages > /dev/null 2>&1

# tmp
