#!/usr/bin/perl
use strict;
#Simple Remove Duplicates from text file, Tested on 500mb file
########################
my $file = 'myfile.txt'; #
########################
my %seen = ();
{
local @ARGV = ($file);
local $^I = '.bac';
    while(<>){
    $seen{$_}++;
    next if $seen{$_} > 1;
    print;
    }
}
