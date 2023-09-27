from dataclasses import dataclass
from typing import Generator, Union


@dataclass
class Scores:
    first_name: str
    second_name: str
    score: int

    @property
    def name(self):
        return f"{self.first_name} {self.second_name}"

    @classmethod
    def build_from_line(cls, row: list[str]) -> 'Scores':
        return cls(
            first_name=row[0],
            second_name=row[1],
            score=int(row[2])
        )


def main(filepath: str, delimiter: str = ",", has_header: bool = True):
    data = read_csv(filepath, delimiter, has_header)
    score, scorers = get_highest_score(data)
    for s in scorers:
        print(f"{s}")
    print(score)


def read_csv(filepath: str, delimiter: str = ",", has_header: bool = True):
    with open(filepath, "+r") as file:
        if has_header:
            next(file)
        for line in file:
            row = [e.strip() for e in line.split(delimiter)]
            yield Scores.build_from_line(row)


def get_highest_score(score_data: Union[list[Scores], Generator[Scores, None, None]]) -> tuple[int, list[str]]:
    highest_score: int = 0
    highest_scorers: list[Scores] = []
    for person in score_data:
        if person.score > highest_score:
            highest_scorers = [person]
            highest_score = person.score
        elif person.score == highest_score:
            highest_scorers.append(person)
    high_scorers = [hs.name for hs in sorted(highest_scorers, key=lambda x: x.first_name)]
    return highest_score, high_scorers


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
