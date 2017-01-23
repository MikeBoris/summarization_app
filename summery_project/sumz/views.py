from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("""

<link href="https://fonts.googleapis.com/css?family=Bungee+Shade|Open+Sans" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Open+Sans|Oswald" rel="stylesheet">

<style>

body {
  background: #1e7a90;
  color: #fff;
  font-family: 'Open Sans', sans-serif;
  text-align: center;
}

h1 {
  font-family: 'Oswald', sans-serif;
  width: 100%;
  text-align: center;
  letter-spacing: 0.02em;
  margin: 2em 0;
}

.textarea {
    width: 50%;
    height: 150px;
    padding: 12px 20px;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
    background-color: #f8f8f8;
    font-size: 16px;
    resize: True;
}

.textboxid {
	background-color:#FFF;
	height:500px;
    font-size:14pt;
}
  .gray-text {
    color: gray;
  }

  h2 {
    font-size: 16px;
    font-family: 'Open Sans', sans-serif;
    line-height: 1.0;
    max-width: 400px;
  }

  p {
    font-size: 16px;
    font-family: 'Open Sans', sans-serif;
  }

</style>

<head>
  <meta charset="UTF-8">
  <title>Summery</title>
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">  
</head>
<body>

<h1>Summarizationalism</h1>

<p>
Maybe: a news aggregator that scores news based on the occurrence of certain words; or that evaluates the circulation of an article (the article's 'community')  by measuring the diversity in demographic profiles (ie the diversity of social networks); or
</p>
</body>

<form name="input_text" action="/cgi-bin/form_test.py" method="get">
<input type="text" class="textarea", name="summarize">
<input type="submit" value="Submit">
</form>

<br>
<br>
<br>
<h2>About</h2>
<p>Summaries generated using a combination of: 

<ul style="list-style-type:circle">
  <li><a href="https://github.com/davidadamojr/TextRank">TextRank</a></li>
  <li><a href="https://github.com/aneesha/RAKE">RAKE</a></li>
  <li><a href="https://gist.github.com/shlomibabluki/5473521">naive summarization</a></li>
</ul>
</p>


""")

