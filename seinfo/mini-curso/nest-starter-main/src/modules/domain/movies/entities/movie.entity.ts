import {Column, Entity, ManyToMany, ManyToOne, OneToMany} from "typeorm";

@Entity()
export class MovieEntity extends BaseEntity{
    @Column()
    name: string;

    @Column()
    descripition: string;

    @ManyToMany(() => MovieEntity, (movie) => movie.genres)
    movies: MovieEntity[];
}