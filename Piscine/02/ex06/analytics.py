import sys
from random import randint
import os
from config import num_of_steps
import requests
import json
import logging

class Research:
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            logging.warning('Calculating the counts of heads and tails')
            heads = 0
            tails = 0
            for peace in self.data:
                heads += peace[0]
                tails += peace[1]
            return heads, tails
        def fractions(self):
            logging.warning('Calculating the fractions of heads and tails')
            heads, tails = self.counts()
            return heads * 100 / (heads + tails), tails * 100/ (heads + tails)

    
    def __init__(self, file_name):
        self.file_name = file_name

    def check_file_header(self, origin, line):
        check = line.split(',')
        if not line or len(check) != 2:
            raise Exception('Bad file header')
        if origin[0][-1].isspace() or origin[0][0].isspace() or (len(origin[1]) > 1 and origin[1][0].isspace()) or origin[1][-1] != '\n':
            raise Exception('Bad file content', "Bad header alignment")
        if len(origin[1]) > 2 and origin[1][-2].isspace():
            raise Exception('Bad file content', "Bad header alignment")
            

    def check_content_alignent(self, line):
        if len(line[0]) > 1 or (len(line[1]) > 2 and line[1][1] != '\n'):
            raise Exception('Bad file content', "Bad data alignment")

    def validate_content(self, content):
        if len(content) != 2:
            raise Exception('Bad file content', 'Not enougth data content')
        if not content[0].isnumeric() or not content[1].isnumeric():
            print(content[0], not content[0].isdigit(), content[1], not content[1].isdigit())
            raise Exception('Bad file content', "Table data must be digital")
        if int(content[0]) not in (1, 0) or int(content[1]) not in (1, 0):
            raise Exception('Bad file content', "Data content must be 0 or 1")
        if int(content[0]) == int(content[1]):
            raise Exception('Bad file content', "(contains equel numbers)")
        return [int(content[0]), int(content[1])]
    
    def file_reader(self, has_header=True):
        logging.warning(f'Reading data from {self.filename}')
        with open(self.file_name, "r") as file:
            line = file.readline()
            if line and has_header:
                self.check_file_header(line.split(','), line.strip())
                line = file.readline()
            strs = 0
            data = []
            while line:
                strs += 1
                self.check_content_alignent(line.split(','))
                data += [self.validate_content(line.strip().split(','))]
                line = file.readline()
            if strs < 1:
                raise Exception('File has no content')
            return data
    def SendReport(success=True):
        logging.warning(f'Sending report to slack workspace')
        webhook_url = 'https://hooks.slack.com/services/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'
        if (success):
            slack_data = {'text': "The report has been successfully created"}
        else:
            slack_data = {'text': "The report hasn’t been created due to an error"}
        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError('Request to slack returned an error %s, the response is:\n%s'
                    %(response.status_code, response.text))

class Analitics(Research.Calculations):
    def predict_random(self):
        logging.warning(f'Predicting random heads and tails')
        i = 0
        predictions = []
        while i < num_of_steps:
            predict = randint(0, 1)
            predictions += [[predict, 0 if predict == 1 else 1]]
            i += 1
        return predictions
    def predict_last(self):
        logging.warning(f'Predicting last head and tail')
        return self.data[-1]
    
    def save_file(self, data, name, ext):
        logging.warning(f'Saving file {name}')
        with open('./' + name + '.' + ext, 'w+') as file:
            file.write(data)

def CheckArguments(av):
    if len(av) != 1:
        raise Exception('Wrong argument', "The argument number is not one")
