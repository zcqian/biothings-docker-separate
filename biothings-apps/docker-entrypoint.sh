#!/bin/bash

function stop()
{
    echo "Stopping ..."
    kill -INT $biothings_pid
}

trap stop SIGTERM SIGINT
