#tmux \
#new-session "/bin/sh -c 'echo 'Hello guys'; exec bash'" \; \
#split-window -h "/bin/sh -c 'echo 'This program will help us'; exec bash'" \; \
#split-window -h "/bin/sh -c 'echo 'to work in seperate terminals'; exec bash'" \; \
#split-window -v "/bin/sh -c 'echo 'at the same time'; exec bash'" \; \
#attach


tmux \
new-session "/bin/sh -c 'echo "Hello_guys";echo "Tmux_is_a_nice_tool"; exec bash'" \; \
split-window "/bin/sh -c 'echo "This_program_will_help_us"; exec bash'" \; \
split-window "/bin/sh -c 'echo "to_work_in_seperate_terminals"; exec bash'" \; \
split-window "/bin/sh -c 'bash ./additional_script.sh; exec bash'" \; \
select-layout even-horizont



#split-window -v "/bin/sh -c 'bash /home/alex/Desktop/echo_script.sh; exec bash'" \; \
#split-window -h "/bin/sh -c 'bash /home/alex/Desktop/echo_script.sh; exec bash'" \; \