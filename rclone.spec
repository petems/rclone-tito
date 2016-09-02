BuildArch:     x86_64
Name:          rclone
Version:       1.36
Release:       1
License:       MIT
Group:         optional
Summary:       Rclone

URL:           http://rclone.org/
Packager:      Peter Souter <webmaster@petersouter.co.uk>

Prefix:        /
Conflicts:     rclone
Obsoletes:     rclone
Provides:      rclone = v1.33
Provides:      rclone(x86-64) = 1.33
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#suggest
#enhance
%description
Rclone
%install
%prep
%build
%clean
rm -rf "/usr/bin/rclone"
rm -rf "/usr/share/man/man1/rclone.1"
%files
%defattr(644,root,root,755)
%attr(0755, root, root) %{_bindir}/rclone
%doc %attr(0644, root, root) %{_mandir}/rclone.1
%changelog
* Fri Sep 02 2016 Unknown name 1.36-1
- new package built with tito

