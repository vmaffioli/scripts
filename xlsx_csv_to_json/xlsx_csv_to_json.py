{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insira o caminho do arquivo:teste.xlsx\n",
      "ok excel\n",
      "fim\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import re\n",
    "\n",
    "path = input('Insira o caminho do arquivo:')\n",
    "\n",
    "if len(path) > 0:\n",
    "    if re.search('\\\\b.xlsx\\\\b', path, re.IGNORECASE):\n",
    "        df_excel = pd.read_excel(path)\n",
    "        df_excel.to_json(path.replace(\".xlsx\", \".json\"))\n",
    "        \n",
    "    elif re.search('\\\\b.csv\\\\b', path, re.IGNORECASE):\n",
    "        df_csv = pd.read_csv(path)\n",
    "        df_csv.to_json(path.replace(\".csv\", \".json\"))\n",
    "        \n",
    "    else:\n",
    "        print('Arquivo invalido')\n",
    "\n",
    "else:\n",
    "    print('Arquivo invalido')\n",
    "    \n",
    "    \n",
    "\n",
    "    \n",
    "    \n",
    "\n",
    "\n",
    "\n"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
