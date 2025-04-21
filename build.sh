
# change to output of pwd
origin="/home/merzouka/esi/security/presentation/demo"
path="$origin/src/legit"
package=$(cat "$path/pyproject.toml" | grep -E '^name' | awk -F ' = ' '{print $2}' | tr -d '"')

echo "Removing dist folder..."
rm -r "$path/dist"
for folder in $(ls $path/src); do
    if [ ! "$folder" = "$package" ]; then
        echo "Removing $folder..."
        rm -r $folder
    fi
done

cd $path
python -m build

