data = """
<section>
    <section>
        <h2>Title1</h2>
        <p>Text1</p>
        <p>Text1</p>
     </section>
  <section>
        <h2>Title2</h2>
        <p>Text2</p>
        <p>Text2</p>
     </section>
  <section>
        <h2>Title3</h2>
        <p>Text3</p>
        <p>Text3</p>
     </section>
  </section>
<section>
        <h2>Title2-1</h2>
        <p>Text2-1</p>
        <p>Text2-1</p>
</section>
<section>
        <h2>Title3-1</h2>
        <p>Text3-1</p>
        <p>Text3-1</p>
</section>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(data)

sections = soup.find_all('section')


for each in sections: #iterate over loop [above sections]
    if each.find('section'):
        continue
    else:
        print each.prettify()