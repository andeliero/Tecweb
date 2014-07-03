<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output omit-xml-declaration="yes" />
    <xsl:template match="recensione">
		<div id="breadcrumb">
			<ul>
				<li><a href="/tecweb/~fros/cgi-bin/home.cgi"><span xml:lang="en">Home</span> >> </a></li>
				<li><a href="show.cgi?type=r">Recensioni >> </a></li>
				<li><xsl:value-of select="titolo"/> </li>
			</ul>
		</div>
                <div id="contents" class="article_box">
                    <a href="/tecweb/~fros/cgi-bin/show.cgi?type=r" class="ribbon RecensioniRibbon">Recensioni</a>
                    <a class="help" href="#footer">salta contenuto</a>
                    <h1>
                        <xsl:copy-of select="titolo/node()"/>
                    </h1>
                    <h2>Scritto da <xsl:value-of select="editore/nome"/>&#160;
                        <xsl:value-of select="editore/cognome"/> il <xsl:value-of select="data"/>
                    </h2>
                    <ul class="tags">
                        <xsl:for-each select="tag">
                            <li>
                                <xsl:element name="a">
                                    <xsl:attribute name="href">/tecweb/~fros/cgi-bin/searchtags.cgi?idtag=<xsl:value-of select="string(@id)" /></xsl:attribute>
                                    <xsl:value-of select="node()"/>
                                </xsl:element>
                            </li>
                        </xsl:for-each>
                    </ul>
                    <xsl:element name="img">
                        <xsl:attribute name="class">article_img</xsl:attribute>
                        <xsl:attribute name='src'>/tecweb/~fros<xsl:value-of select="foto/src/node()"/></xsl:attribute>
                        <xsl:attribute name='alt'>
                            <xsl:value-of select="foto/alt/node()" />
                        </xsl:attribute>
                    </xsl:element>
                   
                    <p id="descrizione">
                        <xsl:copy-of select="descrizione/node()"/>
                    </p>
		<div class="nav_help"><a href="#header">torna su</a></div>
                </div>
		<div class="nav_help"><a href="#header">torna su</a></div>
    </xsl:template>
</xsl:stylesheet>
