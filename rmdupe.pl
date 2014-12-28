#!/usr/bin/perl
use strict;
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
