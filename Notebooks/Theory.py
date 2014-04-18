# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import display, HTML

display(HTML(data="""
<style>

table.presentation, table.verbs, table.patterns, table.verbal_patterns {
    margin-left: auto;
    margin-right: auto;
}

table.presentation, table.presentation tr, table.presentation th, table.presentation td {
    border-style:hidden;
    color: Maroon;
}

table.verbs, table.verbs tr, table.verbs th, table.verbs td {
    border-style:hidden;
    color: Maroon;
    font-size: small;
}

table.patterns, table.patterns tr, table.patterns th, table.patterns td {
    border-style:hidden;
    color: Maroon;
    font-size: small;
}

table.verbal_patterns, table.verbal_patterns tr, table.verbal_patterns th, table.verbal_patterns td {
    border-style:hidden;
    color: Maroon;
}

table.presentation th, table.presentation td, table.patterns th, table.patterns td {
    padding:0px 10px 0px 0px;
}

table.verbs td {
    padding:5px 10px 5px 10px;
}

table.verbal_patterns td {
    border-left-style:dotted;
	border-width-left:thin;
    border-right-style:dotted;
	border-width-right:thin;
}

table.verbs td.dimension {
    text-align:center;
    text-decoration:underline;
}

table.verbs td.form {
    font-style:italic;
    font-weight:bold;
    color:Maroon;
}

table.patterns td.head {
    text-decoration:underline;
}

table.presentation th {
    text-align:center;
}

figure.table {
    text-align:center;
    border-style:dotted;
    border-width:thin;
    max-width:50%;
}

figcaption {
    font-style:italic;
    font-size:x-small;
    text-align:right;
}

span.hebrew, table.presentation td.hebrew {
    text-align:right;
    font-family:SBL Hebrew;
}

table.presentation td.outer {
    vertical-align:top;
}

p.note {
    font-size:small;
    font-style:italic;
}

div.button {
	max-width:15%;
	margin:auto;
}

</style>
"""))

# <codecell>


