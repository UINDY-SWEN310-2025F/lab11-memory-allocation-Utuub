echo "Running tests..."

CUR=$(pwd)
echo $CUR
SCRIPT_DIR=$CUR"/script_test"
TEST_DIR=$CUR"/tests"
ANS_DIR=$CUR"/answer"
echo $SCRIPT_DIR


output1=$(./contiguous <<EOF
3
100
200
300
600300
45
0
0
2
223
123
^C
EOF
)
PIPET1_OUT=$TEST_DIR"/contiguous_out1"
echo "output--contiguous#1"
echo $output1
echo $output1 > $PIPET1_OUT
cat $PIPET1_OUT

output2=$(./contiguous <<EOF
3
200
200
300
611300
45
0
0
3
213
123
673
^C
EOF
)
PIPET2_OUT=$TEST_DIR"/contiguous_out2"
echo "output--contiguous#1"
echo $output2
echo $output2 > $PIPET2_OUT
cat $PIPET2_OUT

# output2=$(./psh2 <<EOF
#   ls
#   -lt
#   ^C
# EOF
# )
# PSH1_OUT=$TEST_DIR"/psh2_out"
# echo $output2 > $PSH1_OUT

echo "Output prepared."

exit 0