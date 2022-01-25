uses
    math, sysutils;

const
    alpha: string = 'abcdefghijklmnopqrstuvwxyz';

    maxm = 10;

var
    p, i, j, n, m, k, t, z: longint;
    pair: array [1..maxm * maxm] of string;
    ind: array [1..maxm, 1..maxm] of boolean;
    s1, s2: string;
    i1, i2, l1, l2: longint;
    ok: boolean;
    c: char;

begin
    n := strtoint(paramstr(1));
    m := strtoint(paramstr(2));
    p := 50;
    z := 10000000;
    randseed := m + n;
    
    for i := 1 to m do
        for j := i + 1 to m do
            if random(100) < p then begin
                ind[i][j] := true;
                ind[j][i] := true;
            end;

    repeat
        i1 := random(m) + 1;
        i2 := random(m) + 1;
    until i1 <> i2;
    ind[i1][i2] := true;
    ind[i2][i1] := true;

    t := 0;
    for i := 1 to m do begin
        for j := i + 1 to m do
            if ind[i][j] then begin
                inc(t); 
                pair[t] := alpha[i] + alpha[j]
            end;
    end;

    repeat
        l1 := random(n);
        l2 := random(n);
    until l1 <> l2;

    s1 := '';
    for i := 1 to l1 do
        s1 := s1 + chr(ord('a') + i1 - 1);
    for i := l1 + 1 to n do
        s1 := s1 + chr(ord('a') + i2 - 1);
    s2 := '';
    for i := 1 to l2 do
        s2 := s2 + chr(ord('a') + i1 - 1);
    for i := l2 + 1 to n do
        s2 := s2 + chr(ord('a') + i2 - 1);


    writeln(m, ' ', t);

    for i := t downto 1 do begin
        j := random(i) + 1;
        writeln(pair[j]);
        pair[j] := pair[i];
    end;

    writeln(s1);
    writeln(s2);
end.