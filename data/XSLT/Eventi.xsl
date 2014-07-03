<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output omit-xml-declaration="yes" />
    <xsl:template match="evento">
                <div id="breadcrumb">
			<ul>
				<li><a href="/tecweb/~fros/cgi-bin/home.cgi"><span xml:lang="en">Home</span> >> </a></li>
				<li><a href="show.cgi?type=e">Eventi >> </a></li>
				<li><xsl:value-of select="titolo"/> </li>
			</ul>
		</div>
                 <div id="contents" class="article_box">
                    <a href="/tecweb/~fros/cgi-bin/show.cgi?type=e" class="ribbon eventRibbon">Eventi</a>
                    <a class="help" href="#footer">salta contenuto</a>
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
                        <xsl:attribute name='src'>/tecweb/~fros<xsl:value-of select="foto/src/node()"/></xsl:attribute>
                        <xsl:attribute name='alt'>
                            <xsl:copy-of select="foto/alt/node()" />
                        </xsl:attribute>
                    </xsl:element>
                    
                    <div id="informazioni">
                     <ul>
                         <li>Città: <strong><xsl:value-of select="luogo"/></strong></li>
                         <li>Ora Inizio: <strong><xsl:value-of select="oraInizio"/></strong></li>
                         <li>Ora Fine: <strong><xsl:value-of select="oraFine"/> </strong></li>
                         <li>Indirizzo: <strong><xsl:value-of select="indirizzo"/></strong></li>
                         <li>Prezzo: <strong><xsl:value-of select="prezzo"/></strong></li>
                         <li>Info email:<strong> <xsl:value-of select="email"/></strong></li>
                         <li>Telefono: <strong><xsl:value-of select="telefono"/></strong></li>
                     </ul>
                     </div>
                    
                   <p id="descrizione">
                        <xsl:copy-of select="descrizione/node()"/>
                    </p>
                <div class="nav_help"><a href="#header">torna su</a></div>  
                </div>
		<div class="nav_help"><a href="#header">torna su</a></div>
                
    </xsl:template>
</xsl:stylesheet>
