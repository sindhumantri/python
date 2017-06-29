#! /usr/bin/python

import os

lines = ['3', 'TF 5', 'There exist birds that can not fly. (true/false)', 'true', 'MC 10', 'Who was the president of the USA in 1991?', '6', 'Richard Nixon', 'Gerald Ford', 'Jimmy Carter', 'Ronald Reagan', 'George Bush Sr.', 'Bill Clinton', 'E', 'SA 20', 'What city hosted the 2004 Summer Olympics?', 'Athens']

# following is the abstract class for TF, MC and SA
class Question(object):
  def __init__(self, question, points, answer):
    self.question = question
    self.points = int(points)
    self.answer = answer
    
  def display_question(self):
    print ("Points: %s" % self.points)
    print ("Question: %s" % self.question)
    
  def validate_answer(self, user_answer):
    if self.answer.lower() == user_answer.lower():
      print ("Correct! you got %s points" % self.points)
      return self.points
    elif user_answer == "SKIP":
      print("You have elected to skip that question.")
      return 0
    else:
      print ("Incorrect answer. Answer is %s You lose %s points" % (self.answer,
                                                                    self.points))
      return -self.points

class QuestionTF(Question):
  def __init__(self, question, points, answer):
    super(QuestionTF, self).__init__(question, points, answer)
      
class QuestionMC(Question):
  def __init__(self, question, points, answer, options):
    super(QuestionMC, self).__init__(question, points, answer)
    self.options = options
  
  def display_question(self):
    print("Points: %s" % self.points)
    print ("Question: %s" % self.question)
    for (opt, val) in self.options:
      print ("%s) %s" %(opt, val))

class QuestionSA(Question):
  def __init__(self, question, points, answer):
    super(QuestionSA, self).__init__(question, points, answer)

class Player():
  def __init__(self, first_name, last_name, points_scored=0):
    self.first_name = first_name
    self.last_name = last_name
    self.points_scored = points_scored

  def add_score(self, val):
    self.points_scored += val

class QuizBowl():
  questions = []

  def run(self):
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    player = Player(first_name, last_name)
    self.load_questions()
    
    err = ("Invalid number. Select from 1-%s" % len(self.questions))
    while True:
      n_questions = input("How many questions would you like (out of %s)?"
                        % len(self.questions))
      try:
        n_questions = int(n_questions)
        if not n_questions or n_questions < 0 or n_questions > len(self.questions):
          print (err)
        else:
          break
      except Exception:
        print (err)
      
    # ask n_questions randomly
    import random
    random.shuffle(self.questions)
    to_ask = self.questions[0:n_questions]
    for q in to_ask:
      q.display_question()
      ans = input()
      points_scored = q.validate_answer(ans)
      player.add_score(points_scored)
      
    print("%s %s, your game is over!\nYou final score is %s points.\nBetter luck next time!" % (player.first_name, player.last_name, player.points_scored))

  def load_questions(self):
    num_questions = 0
    try:
      num_questions = int(lines[0])
    except Exception:
      print ("Invalid number of questions on the first line")
      raise 
    curr_line = 1
    while len(self.questions) < num_questions:
      question_obj = None
      question, answer, choices = "", "", []
      kind, points = lines[curr_line].split(" ")
      curr_line += 1
      #print ("curr_line: %s, type: %s, points: %s" % (curr_line, kind, points))
      if kind == "TF":
        try:
          question, answer = lines[curr_line], lines[curr_line+1]
          curr_line += 2
        except Exception:
          print("Wrong format file")
          raise
        question_obj = QuestionTF(question, points, answer)
      elif kind == "MC":
        try:
          question, num_choices = lines[curr_line], lines[curr_line+1]
          curr_line += 2
          
          options = lines[curr_line:curr_line+int(num_choices)]
          for i, opt in enumerate(options):
            choices.append((chr(65+i), opt))
            
          curr_line += int(num_choices)
          answer = lines[curr_line]
          curr_line += 1
        except Exception:
          print ("Wrong format file")
          raise
        question_obj = QuestionMC(question, points, answer, choices)
      elif kind == "SA":
        try:
          question, answer = lines[curr_line], lines[curr_line+1]
          curr_line += 2
        except Exception:
          print ("Wrong format file")
          raise
        question_obj = QuestionSA(question, points, answer)
      else:
        raise Exception("Unknown question type detected: %s" % kind)
    
      self.questions.append(question_obj)
      
def main():
  quiz = QuizBowl()
  quiz.run()
  
main()
