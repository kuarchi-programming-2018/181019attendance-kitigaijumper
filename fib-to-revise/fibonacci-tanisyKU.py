{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24410294683171395267259945469996127000411199333760853190535535281681195871429510314079442068798555059453792431772087225245168879580469159794544170936403149540819320510882801573596907938222922817134288725100817648047405608500267748766714030468003650259685406411646787207097050545802045736020993909154298598218721111963426993884619351338577630868510716463423585020972878819198991971234596733617320373133963970742975210614209\n"
     ]
    }
   ],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Spyderエディタ\n",
    "\n",
    "これは一時的なスクリプトファイルです\n",
    "\"\"\"\n",
    "\n",
    "    #実験\n",
    "    #F(0) = 0\n",
    "    #F(1) = 1\n",
    "    #F(2) = F(0) + F(1)\n",
    "    #F(3) = F(1) + F(2)\n",
    "\n",
    "#def fib(n):\n",
    "    #return F(n)\n",
    "\n",
    "#def F(m):\n",
    "    #if m == 0:\n",
    "        #return 0\n",
    "    #elif m == 1:\n",
    "        #return 1\n",
    "    #else:\n",
    "        #return F(m-1) + F(m-2)\n",
    "\n",
    "#1から10まで\n",
    "#for i in range(40):\n",
    "    #print(F(i))\n",
    "#print(fib(i))\n",
    "#nを40まで大きくしたら、自己処理とループ処理で時間かかるので、方針転換\n",
    "\n",
    "#代入の=を使い、a = b とb = a + bを利用\n",
    "\n",
    "#実験   \n",
    "#a = 0\n",
    "#b = 1\n",
    "#for i in range(4):\n",
    "     #a = b\n",
    "     #b = a + b\n",
    "     #print(str(a) + \" \" + str(b))\n",
    "#print(b)\n",
    "#c = 0\n",
    "#d = 1\n",
    "#for i in range(4):\n",
    "    #(c, d) = (d, c + d)\n",
    "    #print(str(c) + \" \" + str(d))\n",
    "#print(d)   \n",
    "\n",
    "#これでいけそう\n",
    "#e = 0\n",
    "#f = 1\n",
    "#for i in range(2018):\n",
    "    #(e, f) = (f, e + f)\n",
    "    #print(str(e) + \" \" + str(f))\n",
    "#str(f)\n",
    "#すぐ出てきた\n",
    "\n",
    "def fib(n):\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    elif n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        (a, b) = (0, 1)\n",
    "        for i in range(n - 1):\n",
    "            (a, b) = (b, a + b)\n",
    "        return b\n",
    "    \n",
    "\n",
    "print(fib(2018))\n",
    "#答えは In [31]の出力値\n",
    "\n",
    "    \n",
    "    \n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
