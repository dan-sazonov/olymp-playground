uses
    math, sysutils;

const
    alpha: string = 'abcdefghijklmnopqrstuvwxyz';

    maxm = 10;

var
    q, p, i, j, n, m, k, t, z: longint;
    pair: array [1..maxm * maxm] of string;
    ind: array [1..maxm, 1..maxm] of boolean;
    s1, s2: string;
    ok: boolean;
    c: char;

begin
    n := strtoint(paramstr(1));
    m := strtoint(paramstr(2));
    p := strtoint(paramstr(3));
    q := strtoint(paramstr(4));

    randseed := n + m + p + q;
    
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
    for i := 1 to q do begin
        j := random(n - 1) + 1;
        s2[j] := alpha[random(m) + 1];
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