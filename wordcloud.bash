## Wordcloud of the user commits in the last 30 days
## Usage: wordcloud.bash required: <username> <repo> optional: <branch> <shape of the wordcloud>
## Example: wordcloud.bash "username" "repo" "master" "Github.png"

# Get the username and repo
username=$1
repo=$2
# Get the branch
branch=$3
# Get the shape of the wordcloud
shape=$4

output=$5

# download the repo
git clone $repo

# Perform git log to get the log of his commits
cd $repo
git log --author=$username --pretty=format:"%s" > ../commits.txt

# Install wordcloud
pip install wordcloud

# Generate the wordcloud

python create_wordcloud.py commits.txt $shape $output