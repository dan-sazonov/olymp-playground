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
    ok: boolean;
    c: char;

begin
    n := strtoint(paramstr(1));
    m := strtoint(paramstr(2));
    p := strtoint(paramstr(3));
    z := 10000000;

    randseed := n + m + p;
    
    for i := 1 to m do
        for j := i + 1 to m do
            if random(100) < p then begin
                ind[i][j] := true;
                ind[j][i] := true;
            end;

    t := 0;
    for i := 1 to m do begin
        for j := i + 1 to m do
            if ind[i][j] then begin
                inc(t); 
                pair[t] := alpha[i] + alpha[j]
            end;
    end;

    s1 := '';
    for i := 1 to n do begin
        c := alpha[random(m) + 1];
        s1 := s1 + c;
    end;

    s2 := s1;
    for i := 1 to z do begin
        j := random(n - 1) + 1;
        if ind[ord(s2[j]) - ord('a') + 1][ord(s2[j + 1]) - ord('a') + 1] then begin
            c := s2[j];
            s2[j] := s2[j + 1];
            s2[j + 1] := c;
        end;
    end;

    writeln(m, ' ', t);

    for i := t downto 1 do begin
        j := random(i) + 1;
        writeln(pair[j]);
        pair[j] := pair[i];
    end;

    writeln(s1);
    writeln(s2);
end.