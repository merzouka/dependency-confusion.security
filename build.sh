
# change to output of pwd
origin="/home/merzouka/esi/security/presentation/demo"
path="$origin/src/legit"
package=$(cat "$path/pyproject.toml" | grep -E '^name' | awk -F ' = ' '{print $2}' | tr -d '"')

if [ -d "$path/dist" ]; then
    echo "Removing dist folder..."
    rm -r "$path/dist"
fi

for folder in $(ls $path/src); do
    if [ ! "$folder" = "$package" ]; then
        echo "Removing $folder..."
        rm -r $folder
    fi
done

cd $path
python -m build

cd $origin
if [ -L $origin/packages/$package ]; then
    echo "Removing old symbolic link..."
    rm $origin/packages/$package
    exit
fi

echo "Creating symbolic link..."
ln -s $path/dist $origin/packages/$package
