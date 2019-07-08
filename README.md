# backend-simple-web-scraper

Today you'll write a command line program to scrape a single web page, extracting any URLs, email addresses, and phone numbers it contains.

    Use the argparse (Links to an external site.)Links to an external site. library to parse a URL passed in as a command line argument.
    Use the requests (Links to an external site.)Links to an external site. library to retrieve the text of the webpage at the specified URL.
    Use the re (Links to an external site.)Links to an external site. library to look for email addresses, URLs, and phone numbers included in the page.

Example command

$ python scraper.py https://nookpaleo.com

Example output

URLs
  ...
https://6ncn8s99js-flywheel.netdna-ssl.com/wp-content/uploads/2018/01/paleo-influenced-diner-indianapolis-indiana.png
https://6ncn8s99js-flywheel.netdna-ssl.com/wp-content/uploads/2018/02/about-eating-paleo-indianapolis-indiana.jpg
https://6ncn8s99js-flywheel.netdna-ssl.com/wp-content/uploads/2018/02/about-our-paleo-influenced-diner-downtown-indy.jpg
https://6ncn8s99js-flywheel.netdna-ssl.com/wp-content/uploads/2018/02/nook-paleo-gluten-free-vegan-menu-options.jpg
https://6ncn8s99js-flywheel.netdna-ssl.com/wp-content/uploads/2018/02/nook-paleo-private-party-event-room-400x284.jpg
  ...
https://nookpaleo.com/comments/feed/
https://nookpaleo.com/contact/
https://nookpaleo.com/faqs/
https://nookpaleo.com/feed/
https://nookpaleo.com/hiring/
  ...
https://www.indianapolismonthly.com/dining-blog/the-25-best-tacos-in-indianapolis/
https://www.instagram.com/nookpaleo/
  ...

Phone Numbers
317-759-3554

The ellipses ("...") in the above example denote sections of the output that have been omitted for brevity.
Note on parsing HTML

In general, regular expressions are not well suited for parsing HTML. In this case, the patterns you are looking for are relatively simple. Try using re.findall together with the regular expressions from:

    urlregex.com (Links to an external site.)Links to an external site.
    emailregex.com (Links to an external site.)Links to an external site.
    phoneregex.com (Links to an external site.)Links to an external site.

You may find you need to tweak the patterns a bit for your application. For example, if you're using re.findall to search for emails in a large block of text, your pattern shouldn't use the ^ and $ meta-characters to limit matches to the full string.

You should be able to get some useful initial results, but you may also see some spurious results due to regular expressions matching text within <script> blocks, for example.

You can experiment with using regular expressions to strip tags by doing things like:

re.sub(r"<[^>]*>", " ", text)

Before going too far down this path however, you may also find it worthwhile to explore the HTMLParser (Links to an external site.)Links to an external site. library, which can give you more robust options for navigating an HTML document.
Output

Your scraper doesn't have to conform to a specific output format, but running it with a command like:

python scraper.py http://kenzie.academy/

Should output some reasonably formatted text listing the URLs, email addresses, and phone numbers found in the page.