#!/usr/bin/perl -w

use strict;
print ("Content-type: text/html\n\n <html><head><title>HelloWorld</title></head><body>");
print "<h1>Ciao Scemi!<h1>";
my ($values);
foreach (sort(keys(%ENV)))
{
$values.="<tr><td>$_</td><td>$ENV{$_}</td></tr>\n";
}
print <<EOF;
<h1>Hello World</h1>
<table><tr><th>Env.Variable</th><th>Values</th>\n$values</table>
<tr><p>These are the server's environment variables. Hope this helps to start all: see >perldoc perldoc as a starting point</p>
</body></html>

EOF

exit 0;