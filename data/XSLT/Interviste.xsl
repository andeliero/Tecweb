<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output omit-xml-declaration="yes"/>
    <xsl:template match="intervista">
		<div id="breadcrumb">
			<ul>
				<li><a href="/tecweb/~fros/cgi-bin/home.cgi"><span xml:lang="en">Home</span> >> </a></li>
				<li><a href="show.cgi?type=i">Interviste >> </a></li>
				<li><xsl:value-of select="titolo"/> </li>
			</ul>
		</div>
                <div id="contents" class="article_box">
                    <a href="/tecweb/~fros/cgi-bin/show.cgi?type=i" class="ribbon intervisteRibbon">Interviste</a>
                    <h1>
                        <xsl:copy-of select="titolo/node()"/>
                    </h1>
                    <a class="help" href="#footer">salta contenuto</a>

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
                    <h3 id="interlocutore">Abbiamo intervistato: <xsl:value-of select="intervistato"/></h3>
                    <p id="descrizione">
                        <xsl:copy-of select="descrizione/node()"/>
                    </p>
                    <div class="nav_help"><a href="#header">torna su</a></div>
                    <p id="Titologallery" class="notAural">GALLERY</p>

                                       
                    <xsl:if test="galleria">
                        <div id="gallery" class="notAural" >
                            <ul>
                                <xsl:if test="//galleria/foto[1]">
                                    <li id="img1" class="active">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[1]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[1]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>

                                <xsl:if test="//galleria/foto[2]">
                                    <li id="img2" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[2]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[2]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                
                                <xsl:if test="//galleria/foto[3]">
                                    <li id="img3" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[3]/srcPath/node()"/></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[3]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                
                                <xsl:if test="//galleria/foto[4]">
                                    <li id="img4" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[4]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[4]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                <xsl:if test="//galleria/foto[5]">
                                    <li id="img5" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[5]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[5]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                
                                <xsl:if test="//galleria/foto[6]">
                                    <li id="img6" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[6]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[6]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                
                                <xsl:if test="//galleria/foto[7]">
                                    <li id="img7" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[7]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[7]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                
                                <xsl:if test="//galleria/foto[8]">
                                    <li id="img8" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[8]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[8]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                                
                                <xsl:if test="//galleria/foto[9]">
                                    <li id="img9" class="hidden">
                                        <xsl:element name="img">
                                            <xsl:attribute name="class">slide</xsl:attribute>
                                            <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[9]/srcPath/node()" /></xsl:attribute>
                                            <xsl:attribute name="alt">
                                                <xsl:copy-of select="//galleria/foto[9]/titolo/node()" />
                                            </xsl:attribute>
                                        </xsl:element>
                                    </li>
                                </xsl:if>
                            </ul>
                            
                            <div id="prev">
                                <button class="galleryButton" title="Precedente" onclick="previous();" type="button">Precedente</button>
                            </div>
                            <div id="next">
                                <button class="galleryButton" title="Prossima" onclick="next();" type="button">Prossima</button>
                            </div>
                        </div>
                        
                        <ol id="controlnav" >
                            <xsl:if test="//galleria/foto[1]">
                                <li id="t1" class="activenav">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[1]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[1]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(1)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[2]">
                                <li id="t2">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[2]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[2]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(2)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[3]">
                                <li id="t3">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[3]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[3]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(3)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[4]">
                                <li id="t4">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[4]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[4]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(4)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[5]">
                                <li id="t5">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[5]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[5]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(5)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[6]">
                                <li id="t6">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[6]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[6]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(6)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[7]">
                                <li id="t7">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[7]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[7]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(7)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[8]">
                                <li id="t8">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[8]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[8]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(8)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                            <xsl:if test="//galleria/foto[9]">
                                <li id="t9">
                                    <xsl:element name="img">
                                        <xsl:attribute name="class">tnail</xsl:attribute>
                                        <xsl:attribute name="src">/tecweb/~fros<xsl:copy-of select="//galleria/foto[9]/srcPath/node()" /></xsl:attribute>
                                        <xsl:attribute name="alt">
                                            <xsl:copy-of select="//galleria/foto[9]/titolo/node()" />
                                        </xsl:attribute>
                                        <xsl:attribute name="onclick">change(9)</xsl:attribute>
                                    </xsl:element>
                                </li>
                            </xsl:if>
                            
                        </ol>
                        
                        
                        
                        
                        
                    </xsl:if>
                </div>
		<div class="nav_help"><a href="#header">torna su</a></div>
    </xsl:template>
</xsl:stylesheet>
