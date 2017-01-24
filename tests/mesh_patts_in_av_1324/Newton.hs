-- Author: Anders Claesson <anders.claesson@gmail.com>

module Newton (diff, newtonTriangle, newtonPolynomial) where

-- | First finite differences of a sequence.
diff :: [Int] -> [Int]
diff xs = zipWith (-) (drop 1 xs) xs

-- | The triangle resulting from iterating diff.
newtonTriangle :: [Int] -> [[Int]]
newtonTriangle = takeWhile (not . null) . iterate diff

{-|
  newtonPolynomial [f 0, f 1, f 2, ... ] returns the coefficients of a
  polynomial f that fits the list of values [f 0, f 1, f 2, ... ] given.

  NB: The coefficients are given with respect to the binomial basis
  (rather than the standard basis). E.g.,
  > newtonPolynomial [1,2,5,10,17]
  [1,1,2]
  and so the resulting polynomial is
  1*{n choose 0} + 1*{n choose 1} + 2*{n choose 2} = 1 + n^2
-}
newtonPolynomial :: [Int] -> [Int]
newtonPolynomial =
    reverse . dropWhile (==0) . reverse . map head . newtonTriangle
