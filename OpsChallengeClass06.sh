#!/bin/bash

function SearchDirectory() {
    
    DIRNAME=$1
    FILENAME=$2
    
    if [ ! -d "$DIRNAME" ]
    then
        mkdir $DIRNAME
        echo "Directory $DIRNAME created"
    else
        echo "Directory $DIRNAME exists"
    fi
    
    if [ ! -f "$DIRNAME/$FILENAME" ]
    then
        touch "$DIRNAME/$FILENAME"
        echo "File $DIRNAME/$FILENAME created"
    else
        echo "File $DIRNAME/$FILENAME exists"
    fi
    
}