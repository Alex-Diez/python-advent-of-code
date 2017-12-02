import unittest


def checksum(spreed_sheet):
    check_sum = 0
    for row in spreed_sheet.split('\n'):
        numbers = row.split('\t')
        max_num = int(numbers[0])
        min_num = int(numbers[0])
        for index in range(1, len(numbers)):
            num = int(numbers[index])
            if max_num < num:
                max_num = num
            if min_num > num:
                min_num = num
        check_sum += max_num - min_num
    return check_sum


class CheckSumTest(unittest.TestCase):
    def testCheckSumOfOnes(self):
        self.assertEqual(0, checksum('1\t1\t1\n1\t1\t1\t1\n1\t1\t1'))

    def testCheckSumOfSingleDiff(self):
        self.assertEqual(1, checksum('1\t1\t1\n1\t2\t1\t1\n1\t1\t1'))

    def testTaskInput(self):
        task_input = """5\t1\t9\t5
7\t5\t3
2\t4\t6\t8"""
        self.assertEqual(18, checksum(task_input))

    def testPrintSolution(self):
        test_input = """116\t1259\t1045\t679\t1334\t157\t277\t1217\t218\t641\t1089\t136\t247\t1195\t239\t834
269\t1751\t732\t3016\t260\t6440\t5773\t4677\t306\t230\t6928\t7182\t231\t2942\t2738\t3617
644\t128\t89\t361\t530\t97\t35\t604\t535\t297\t599\t121\t567\t106\t114\t480
105\t408\t120\t363\t430\t102\t137\t283\t123\t258\t19\t101\t181\t477\t463\t279
873\t116\t840\t105\t285\t238\t540\t22\t117\t125\t699\t953\t920\t106\t113\t259
3695\t161\t186\t2188\t3611\t2802\t157\t2154\t3394\t145\t2725\t1327\t3741\t2493\t3607\t4041
140\t1401\t110\t119\t112\t1586\t125\t937\t1469\t1015\t879\t1798\t122\t1151\t100\t926
2401\t191\t219\t607\t267\t2362\t932\t2283\t889\t2567\t2171\t2409\t1078\t2247\t2441\t245
928\t1142\t957\t1155\t922\t1039\t452\t285\t467\t305\t506\t221\t281\t59\t667\t232
3882\t1698\t170\t5796\t2557\t173\t1228\t4630\t174\t3508\t5629\t4395\t180\t5100\t2814\t2247
396\t311\t223\t227\t340\t313\t355\t469\t229\t162\t107\t76\t363\t132\t453\t161
627\t1331\t1143\t1572\t966\t388\t198\t2068\t201\t239\t176\t1805\t1506\t1890\t1980\t1887
3390\t5336\t1730\t4072\t5342\t216\t3823\t85\t5408\t5774\t247\t5308\t232\t256\t5214\t787
176\t1694\t1787\t1586\t3798\t4243\t157\t4224\t3603\t2121\t3733\t851\t2493\t4136\t148\t153
2432\t4030\t3397\t4032\t3952\t2727\t157\t3284\t3450\t3229\t4169\t3471\t4255\t155\t127\t186
919\t615\t335\t816\t138\t97\t881\t790\t855\t89\t451\t789\t423\t108\t95\t116"""
        print(checksum(test_input))


def sum_of_divisible(spreed_sheet):
    check_sum = 0
    for row in spreed_sheet.split('\n'):
        numbers = row.split('\t')
        check_sum += _check_sum_of_division(numbers)
    return check_sum


def _check_sum_of_division(numbers):
    for i in range(len(numbers)):
        dividend = int(numbers[i])
        for j in range(len(numbers)):
            if i != j:
                divisor = int(numbers[j])
                if dividend % divisor == 0:
                    return dividend / divisor
    return 0


class SumOfEvenlyDivisibleValuesTest(unittest.TestCase):
    def testNoDivisibleValues(self):
        self.assertEqual(0, sum_of_divisible('3\t5'))

    def testDividendAndDivisor(self):
        self.assertEqual(2, sum_of_divisible('2\t4'))

    def testTaskInput(self):
        task_input = """5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5"""
        self.assertEqual(9, sum_of_divisible(task_input))

    def testPrintSolution(self):
        test_input = """116\t1259\t1045\t679\t1334\t157\t277\t1217\t218\t641\t1089\t136\t247\t1195\t239\t834
269\t1751\t732\t3016\t260\t6440\t5773\t4677\t306\t230\t6928\t7182\t231\t2942\t2738\t3617
644\t128\t89\t361\t530\t97\t35\t604\t535\t297\t599\t121\t567\t106\t114\t480
105\t408\t120\t363\t430\t102\t137\t283\t123\t258\t19\t101\t181\t477\t463\t279
873\t116\t840\t105\t285\t238\t540\t22\t117\t125\t699\t953\t920\t106\t113\t259
3695\t161\t186\t2188\t3611\t2802\t157\t2154\t3394\t145\t2725\t1327\t3741\t2493\t3607\t4041
140\t1401\t110\t119\t112\t1586\t125\t937\t1469\t1015\t879\t1798\t122\t1151\t100\t926
2401\t191\t219\t607\t267\t2362\t932\t2283\t889\t2567\t2171\t2409\t1078\t2247\t2441\t245
928\t1142\t957\t1155\t922\t1039\t452\t285\t467\t305\t506\t221\t281\t59\t667\t232
3882\t1698\t170\t5796\t2557\t173\t1228\t4630\t174\t3508\t5629\t4395\t180\t5100\t2814\t2247
396\t311\t223\t227\t340\t313\t355\t469\t229\t162\t107\t76\t363\t132\t453\t161
627\t1331\t1143\t1572\t966\t388\t198\t2068\t201\t239\t176\t1805\t1506\t1890\t1980\t1887
3390\t5336\t1730\t4072\t5342\t216\t3823\t85\t5408\t5774\t247\t5308\t232\t256\t5214\t787
176\t1694\t1787\t1586\t3798\t4243\t157\t4224\t3603\t2121\t3733\t851\t2493\t4136\t148\t153
2432\t4030\t3397\t4032\t3952\t2727\t157\t3284\t3450\t3229\t4169\t3471\t4255\t155\t127\t186
919\t615\t335\t816\t138\t97\t881\t790\t855\t89\t451\t789\t423\t108\t95\t116"""
        print(sum_of_divisible(test_input))
