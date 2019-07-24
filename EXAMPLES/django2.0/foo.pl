#!/opt/local/bin/perl
use strict;

# r'^herodetails/(?P<hero_name>.*)'

my $pattern = q{r'^(.*?)/\(P<(.*?)>\.\*\)}

sub wanted {
    return unless /^urls.py$/;

    if open(my $fh, "<", $_) {
        while (my $line = <$fh>) {
            if (m/$pattern/) {
                print $1, $2, '\n';
            }
        }
    }
} 
