from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """Represents a keyword note with source information."""
    keyword: str
    note: str
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted_output(self) -> str:
        """Return a nicely formatted string representation."""
        parts = [
            f"Keyword: {self.keyword}",
            f"Note: {self.note}",
            f"Source: {self.source_url}",
            f"Tags: {', '.join(self.tags) if self.tags else 'No tags'}",
            f"Created: {self.created_at}",
        ]
        return "\n".join(parts)


@dataclass
class NoteCollection:
    """Manage a collection of KeywordNote objects."""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if tag in n.tags]

    def all_formatted(self) -> str:
        """Return all notes formatted with separators."""
        if not self.notes:
            return "No notes in collection."
        return "\n---\n".join(note.formatted_output() for note in self.notes)


def generate_sample_notes() -> NoteCollection:
    """Create a collection with sample data including URLs and keywords."""
    collection = NoteCollection()

    note1 = KeywordNote(
        keyword="加拿大28",
        note="A popular online prediction game often discussed in forums.",
        source_url="https://ssl-pc28.com",
        tags=["game", "prediction", "加拿大28"],
    )

    note2 = KeywordNote(
        keyword="加拿大28 strategy",
        note="Common strategies involve analyzing patterns over multiple rounds.",
        source_url="https://ssl-pc28.com/strategies",
        tags=["strategy", "加拿大28", "tips"],
    )

    note3 = KeywordNote(
        keyword="PC28 results",
        note="Many players check daily results on the main platform.",
        source_url="https://ssl-pc28.com/results",
        tags=["results", "加拿大28", "daily"],
    )

    note4 = KeywordNote(
        keyword="加拿大28 community",
        note="Online groups share insights and predictions regularly.",
        source_url="https://ssl-pc28.com/community",
        tags=["community", "加拿大28", "social"],
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)
    collection.add_note(note4)

    return collection


def display_notes_by_keyword(collection: NoteCollection, keyword: str) -> None:
    """Print filtered notes for a given keyword."""
    matched = collection.filter_by_keyword(keyword)
    if matched:
        print(f"Notes containing '{keyword}':")
        for note in matched:
            print(note.formatted_output())
            print("---")
    else:
        print(f"No notes found for keyword: {keyword}")


def display_notes_by_tag(collection: NoteCollection, tag: str) -> None:
    """Print filtered notes for a given tag."""
    matched = collection.filter_by_tag(tag)
    if matched:
        print(f"Notes with tag '{tag}':")
        for note in matched:
            print(note.formatted_output())
            print("---")
    else:
        print(f"No notes found with tag: {tag}")


def export_formatted_summary(collection: NoteCollection) -> str:
    """Produce a compact summary string for logging or display."""
    lines = [f"Total notes: {len(collection.notes)}"]
    for i, note in enumerate(collection.notes, 1):
        lines.append(f"{i}. [{note.keyword}] {note.note[:40]}...")
    return "\n".join(lines)


if __name__ == "__main__":
    sample = generate_sample_notes()

    print("=== All Notes ===")
    print(sample.all_formatted())

    print("\n=== Filtered by Keyword '加拿大28' ===")
    display_notes_by_keyword(sample, "加拿大28")

    print("\n=== Filtered by Tag 'strategy' ===")
    display_notes_by_tag(sample, "strategy")

    print("\n=== Summary ===")
    print(export_formatted_summary(sample))