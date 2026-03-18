#!/bin/bash

install -d $HOME/.openclaw/workspace/skills/
for i in *; do
    # 跳过非目录
    if [ ! -d "$i" ]; then
        continue
    fi

    target="$HOME/.openclaw/workspace/skills/${i}"
    
    # 如果软链接已经存在，跳过
    if [ -L "$target" ]; then
        echo "软链接已存在，跳过: $target"
        continue
    fi

    # 创建软链接
    echo "创建软链接: ln -s '$(pwd)/$i' '$target'"
    ln -s "$(pwd)/$i" "$target"
done

