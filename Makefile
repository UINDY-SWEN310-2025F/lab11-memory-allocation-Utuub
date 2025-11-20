compile1:
	echo "compiling contiguous.c"
	gcc ./answer/contiguous.c -o ./contiguous

compile2:
	echo "do nothing"

compile3:
	echo "do nothing"

compile4:
	echo "do nothing"

test:
	bash ./script_test/test1.sh
	bash ./script_test/test0.sh
	#bash ./script_test/test2.sh

done:
	#rm -rf ./tests/pc_pid_out
	#rm -rf ./tests/mmyfork_out
	echo "finished"

