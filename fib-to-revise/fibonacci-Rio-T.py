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
      "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n",
      "0\n"
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
    "def fib(n):\n",
    "    #フィボナッチ数列を定義する。\n",
    "    if n == 0:\n",
    "        return 0\n",
    "    elif n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        (a, b) = (0, 1)\n",
    "        for i in range(n - 1):\n",
    "            a, b = b, a + b\n",
    "        return b\n",
    "\n",
    "print([fib(i) for i in range(10)]) \n",
    "#n=1,2,3...,10の時のフィボナッチ数列\n",
    "# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]\n",
    "print(fib(0)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
