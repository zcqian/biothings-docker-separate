#!/bin/bash

function bthub_pids()
{
    ps -ef | grep 'python' | grep 'hub.py' | awk '{if ($2 != "1") print $2}'
}


function stop()
{
    echo "Stopping ..."
    for biothings_pid in $(bthub_pids)
    do 
        kill -INT $biothings_pid
    done
}



trap stop SIGTERM SIGINT

eval $@


biothings_pids=$(bthub_pids)
while [ "$biothings_pids" ]
do
    echo "waiting on $biothings_pids ... "
    wait $biothings_pids  # all exited
    # find new pids (if any)
    biothings_pids=$(bthub_pids)
done

wait