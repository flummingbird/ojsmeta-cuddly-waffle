<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:output indent="yes" />
        
    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:template match="records">
        <issue current="false" identification="title" public_id="" published="false">
            <title locale="">
                <xsl:value-of select="record/issue_date"/>
            </title>
            <description locale="">description</description>
            <volume>volume</volume>
            <number>number</number>
            <year>year</year>
            <cover locale="">
                <caption>caption</caption>
                <image>
                    <href mime_type="" src=""/>
                </image>
            </cover>
            <date_published>date_published</date_published>
            <access_date>access_date</access_date>
            <section>
                <title locale="">title</title>
                <abbrev locale="">abbrev</abbrev>
                <identify_type locale="">identify_type</identify_type>
                <policy locale="">policy</policy>
                <xsl:apply-templates/>
            </section>
        </issue>
    </xsl:template>
    
    <xsl:template match="record">
        <title>
            <xsl:value-of select="title"/>
        </title>
        <abstract>
            <xsl:value-of select="teaser"/>
        </abstract>
        <indexing/>
        <sponsor/>
        <author primary_contact="false">
            <firstname>
                <xsl:value-of select="substring-after(auth_1, ', ')"/>
            </firstname>
            <middlename>
                
            </middlename>
            <lastname>
                <xsl:value-of select="substring-before(auth_1, ', ')"/>
            </lastname>
        </author>
        <pages/>
        <date_published>
            <xsl:value-of select="pub_date"></xsl:value-of>
        </date_published>
        <open_access/>
        <galley locale="">
            <label>label</label>
            <file>
                <href mime_type="" src=""/>
            </file>
        </galley>
        <htmlgalley locale=""/>
            
            
            
    </xsl:template>
    
</xsl:stylesheet>