#!/usr/bin/perl

use strict;
use Math::Combinatorics;

use Data::Dumper;

my @orders;
# 期間は100日間
while(<>) {
	chomp;
#	print $_;
	push(@orders,$_);
}

my %limit_days_payments;

for(my $i=1;$i<=16;$i++) {

	my $combinat=Math::Combinatorics->new(
		count=>$i,
		data=>[@orders],
	);

	while(my @combo=$combinat->next_combination) {
		my $limit_days=0;
		my $limit_days_payments=0;

#		print Dumper(@combo)."\n";

		foreach my $combo(@combo) {
			my ($pay,$day)=(split("\,",$combo))[0,1];
			$limit_days+=$day;
			next if($limit_days > 100);
			$limit_days_payments+=$pay;
			
			$limit_days_payments{$limit_days_payments}=$limit_days;
#			push(@payments,$limit_days_payments);
			print "$limit_days\t".$combo."\n";
#			print "$limit_days\t".join("\t",@combo)."\n";
		}
		print "\n";
	}

}
print "=========== max payments ============\n";
foreach my $pay(sort {$b <=> $a} keys %limit_days_payments) {
	print $limit_days_payments{$pay}."\t".$pay."\n";
}
