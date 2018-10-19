{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
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
    "\n",
    "\n",
    "def fib(n):\n",
    "    x=0\n",
    "    y=1\n",
    "    z=x+y\n",
    "    for i in range(n):\n",
    "        z=x+y\n",
    "        x=y\n",
    "        y=z\n",
    "    return x\n",
    "            \n",
    "\n",
    "print(fib(2018)) "
   ]
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
