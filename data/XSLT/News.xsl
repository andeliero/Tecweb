<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>
    <xsl:template match="item">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                <meta name="author" content="Fabio Ros, Valerio Burlin, Stefano Munari, Alberto Andeliero"/>
                <meta name="language" content="italian it"/>
                <meta name="rating" content="safe for kids" />
                <meta name="description" content="Il portale di news, articoli, recensioni ed eventi dedicato alla musica"/>
                <meta name="keywords" content="musica, news, news musicali, notizie, album"/>
                <xsl:element name="meta">
                    <xsl:attribute name='name'>keywords</xsl:attribute>
                    <xsl:attribute name='content'>
                        <xsl:for-each select="tag">
                            <xsl:copy-of select="node()" />&#160;
                        </xsl:for-each>
                    </xsl:attribute>
                </xsl:element>
                <meta name="robots" content="all" />
                <link rel="icon" href="/tecweb/~fros/img/fav.ico" type="image/icon" />
                <link rel="stylesheet" type="text/css" media="handheld, screen" href="/tecweb/~fros/css/screen.css"/>
                <link rel="stylesheet" type="text/css" media="print" href="/tecweb/~fros/css/print.css"/>
                <link rel="stylesheet" type="text/css" media="speech" href="/tecweb/~fros/css/aural.css"/>
                <title>News - <xsl:value-of select="titolo"/></title>
		      <script type="text/javascript" src="/tecweb/~fros/javascript/screen.js"></script>
            </head>
            <body onload="defsearch();">
                <div id="header">
            <a class="help" href="#nav">salta intestazione</a>
            <div id="title">
                <span id="logo" class="notAural">
                    <a href="/tecweb/~fros/cgi-bin/home.cgi">
                    <img src="/tecweb/~fros/img/tazza-di-caffe.jpg" alt="Tazza di caffè fumante in cui viene immersa  una pausa di semiminima"/>
                    </a>
                </span>
                <h1><a href="/tecweb/~fros/cgi-bin/home.cgi"><span xml:lang="en">Music Break</span></a></h1>
                <h2>Il portale di notizie dedicato alla musica</h2>
            </div>
        </div>
                <div id="nav">
                    <a class="help" href="#contents">salta menù</a>
                    <ul>
                        <li>
                            <a href="/tecweb/~fros/home.xml">
                                <p xml:lang="en">Home</p>
                            </a>
                        </li>
                        <li>
                            <a href="/tecweb/~fros/cgi-bin/show.cgi?type=n">
                                <span xml:lang="en">News</span>
                            </a>
                        </li>
                        <li>
                            <a href="/tecweb/~fros/cgi-bin/show.cgi?type=i">Interviste</a>
                        </li>
                        <li>
                            <a href="/tecweb/~fros/cgi-bin/show.cgi?type=r">Recensioni</a>
                        </li>
                        <li>
                            <a href="/tecweb/~fros/cgi-bin/show.cgi?type=e">Eventi</a>
                        </li>
                    </ul>
                    <div id='search'>
                        <form action='$path/cgi-bin/searchtags.cgi?' method='get'>
                        <input type='text' name='tag' title='inserire una ricerca' id='text_field' onclick='searchbar();' onblur='defsearch();' value=''></input>
                        <input type='submit' id='button' alt='Cerca' value='Cerca'></input>
                        </form>
                    </div>
                </div>
                <div id="contents" class="article_box">
                    <a href="/tecweb/~fros/cgi-bin/show.cgi?type=n" class="ribbon newsRibbon">News</a>
                    <a class="help" href="#sidebar">salta contenuto</a>
                    <h1>
                        <xsl:value-of select="titolo"/>
                    </h1>
                    <h2>Scritto da <xsl:value-of select="editore/nome"/>&#160;
                        <xsl:value-of select="editore/cognome"/> il <xsl:value-of select="data"/>
                    </h2>
                    <ul class="tags">
                        <xsl:for-each select="tag">
                            <li>
                                <xsl:element name="a">
                                    <xsl:attribute name="href">/tecweb/~fros/cgi-bin/searchtags.cgi?idtag=<xsl:copy-of select="string(@id)" /></xsl:attribute>
                                    <xsl:value-of select="node()"/>
                                </xsl:element>
                            </li>
                        </xsl:for-each>
                    </ul>
                    <xsl:element name="img">
                        <xsl:attribute name="class">article_img</xsl:attribute>
                        <xsl:attribute name='src'>
                            /tecweb/~fros<xsl:copy-of select="foto/src/node()" />
                        </xsl:attribute>
                        <xsl:attribute name='alt'>
                            <xsl:copy-of select="foto/alt/node()" />
                        </xsl:attribute>
                    </xsl:element>
                    
                    <p id="descrizione">
                        <xsl:value-of select="descrizione"/>
                    </p>
                </div>
                <div id="footer">
                <a class="help" href="#header">salta testo a fine pagina</a>
                <a href="http://validator.w3.org/check?uri=referer">
                    <img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict"/></a>
                <a href="http://jigsaw.w3.org/css-validator/check/referer"><img src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="CSS Valido!" /></a>
                <p>&#169; 2014 <span xml:lang="en">Music Break All Right Reserved.</span> | 
                <a href="/tecweb/~fros/chi_siamo.html"> Chi siamo</a> | 
                <a href="/tecweb/~fros/condizioni.html">Condizioni d'uso</a> | 
                <a href="/tecweb/~fros/contatti.html"> Contatti</a>  
            </p>
        </div>
        </body>
    </html>
    </xsl:template>
</xsl:stylesheet>
