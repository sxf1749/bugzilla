#!/usr/bin/perl -T
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# This Source Code Form is "Incompatible With Secondary Licenses", as
# defined by the Mozilla Public License, v. 2.0.

use 5.10.1;
use strict;
use warnings;

use lib qw(. lib);

use Bugzilla;
use Bugzilla::Constants;
use Bugzilla::Error;
use Data::UUID ();

my $cgi = Bugzilla->cgi;
my $user = Bugzilla->login(LOGIN_REQUIRED);
my $dir = '/var/www/html/bugzilla/img';
my $file = $cgi->param('dataTempFile');
my $uuid=Data::UUID->new->create_str;
$file=~m/^.*(\\|\/)(.*)/;
my $name = $2;
open(OUTFILE, ">$dir/$uuid$name") or print '0001';
binmode(OUTFILE);
while (read($file, my $buffer, 1024)) {
        print OUTFILE $buffer;
}
close(OUTFILE);
print $cgi->header();
print "$uuid$name";
