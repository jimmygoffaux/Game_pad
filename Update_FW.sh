#!/bin/bash

while true; do
    echo "Press 'Enter' to update slider or 'esc' to quit..."
    while true; do
        read -n 1 -s key
        if [ "$key" = '' ]; then
			sudo python /home/tester/Desktop/KNX_updater/StartDFU.py
		elif [ "$key" = $'\e' ]; then
			read -n 2 -s rest
			if [ "$rest" = '[A' ] || [ "$rest" = '[B' ] || [ "$rest" = '[C' ] || [ "$rest" = '[D' ]; then
				continue
        else
            echo "Sortie..."
            exit 0
        fi
    fi
    done
done


