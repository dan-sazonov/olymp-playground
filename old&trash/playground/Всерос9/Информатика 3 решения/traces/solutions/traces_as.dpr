{$R+,Q+,O-}
program traces;

uses
    sysutils;

const
    maxl = 100000;
    maxc = 'j';

type
    tarr = array [1..maxl] of char;

var
    a: array ['a'..maxc, 'a'..maxc] of boolean;

procedure canonize(const s: string; var z: tarr);
var
    f: array [1..maxl] of longint;
    u: array [1..maxl] of boolean;
    p: array ['a'..maxc] of longint;
    c: char;
    i, j, k, l: longint;
    
begin
    fillchar(p, sizeof(p), 0);

    for i := length(s) downto 1 do begin    
        j := i - 1;
        while (j > 0) and (a[s[i]][s[j]]) do
            dec(j);
        f[i] := j;
        p[s[i]] := i;
    end;

    fillchar(u, sizeof(u), 0);
    l := length(s);
    for i := 1 to l do begin
        z[i] := '?';
        for c := 'a' to maxc do begin
            if p[c] <> 0 then begin
                j := p[c];
                while (f[j] <> 0) and u[f[j]] do begin
                    if s[f[j]] = c then
                        f[j] := 0
                    else begin
                        k := f[j];
                        dec(k);
                        while (k > 0) and ((u[k] and not (s[k] = c)) or a[s[k]][c]) do
                            dec(k);
                        f[j] := k;
                    end;
                end;
                if f[j] = 0 then begin
                    u[j] := true;
                    z[i] := s[j];
                    inc(j);
                    while (j <= l) and (s[j] <> c) do 
                        inc(j);
                    if j <= l then
                        p[c] := j
                    else
                        p[c] := 0;
                    break;
                end;
            end;
        end;
        assert(z[i] <> '?');
    end;
end;

procedure quitno;
begin
    writeln('NO');
    close(output);
    halt(0);
end;

var
    n, m, l: longint;
    i: longint;
    c, d: char;
    s1, s2: string;
    c1, c2: tarr;

begin
    readln(n, m);
    assert(n >= 2);
    assert(n <= 10);

    for i := 1 to m do begin
        read(c);
        read(d);

        assert(c in ['a'..maxc]);
        assert(ord(c) - ord('a') < n);
        assert(d in ['a'..maxc]);
        assert(ord(d) - ord('a') < n);
        assert(c <> d);       
        assert(not a[c][d]);
    
        a[c][d] := true;
        a[d][c] := true;

        assert(eoln);
        readln;
    end;

    readln(s1);
    readln(s2);

    assert(length(s1) >= 1);
    assert(length(s1) <= maxl);
    assert(length(s2) >= 1);
    assert(length(s2) <= maxl);
    for i := 1 to length(s1) do begin
        assert(s1[i] in ['a'..maxc]);
        assert(ord(s1[i]) - ord('a') < n);
    end;
    for i := 1 to length(s2) do begin
        assert(s2[i] in ['a'..maxc]);
        assert(ord(s2[i]) - ord('a') < n);
    end;

    if length(s1) <> length(s2) then
        quitno;

    l := length(s1);

    canonize(s1, c1);
    canonize(s2, c2);

{    for i := 1 to l do
        write(c1[i]);
    writeln;
    for i := 1 to l do
        write(c2[i]);
    writeln;}

    for i := 1 to l do begin
        if c1[i] <> c2[i] then
            quitno;
    end;

    writeln('YES');
end.
